#
# Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES
#
# SPDX-License-Identifier: Apache-2.0
#

__all__ = ['ComputeType', 'Matmul', 'create_handle', 'destroy_handle', 'matmul']

# TODO: check which imports are not needed, once the code is refactored.
import copy
from dataclasses import dataclass
import functools
import logging
import operator
from typing import Sequence

import cupy as cp
import numpy as np

from nvmath.bindings import cublas as cublas
from nvmath.bindings import cublasLt as cublaslt
from nvmath.linalg import configuration
from nvmath import memory

from nvmath._internal import formatters
from nvmath._internal import tensor_wrapper
from nvmath._internal import typemaps
from nvmath._internal import utils

from nvmath.linalg import algorithm

from nvmath.linalg._internal import matmul_desc_ifc, matmul_pref_ifc, matrix_layout_ifc
from nvmath.linalg._internal.typemaps import NAME_TO_DEFAULT_SCALE_TYPE, SCALE_TYPE_TO_COMPUTE_TYPE
from nvmath.linalg._internal.utils import create_handle, destroy_handle, get_handle, pointer_aligned_to

# TODO: move the map to _internal.
from nvmath.linalg.configuration import Epilogue
from nvmath.linalg._internal.epilog_protocol import BiasHandler
EPILOG_HANDLERS_MAP = {Epilogue.RELU: [], Epilogue.GELU: [], Epilogue.BIAS: [BiasHandler], Epilogue.RELU_BIAS: [BiasHandler], Epilogue.GELU_BIAS: [BiasHandler]}
EPILOG_FLOP_COUNT_MAP = {
    Epilogue.RELU: lambda m, n: m * n,
    Epilogue.GELU: lambda m, n: 0,    # TODO
    Epilogue.BIAS: lambda m, n: m * n,
    Epilogue.RELU_BIAS: lambda m, n: 2 * m * n,
    Epilogue.GELU_BIAS: lambda m, n: m * n     # TODO
}

ComputeType = cublas.ComputeType

# TODO: place common utility functions for FFT, linear algebra, ... in a module.
def get_null_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(logging.NullHandler())
    logger.propagate = False

    return logger

def _contiguous_layout(sorted_shape, sorted_strides):
    for s in range(1, len(sorted_strides)):
        if sorted_shape[s-1] * sorted_strides[s-1] != sorted_strides[s]:
            return False
    return True

def check_batch_tileable(sorted_batch_shape, sorted_batch_strides):
    """
    Check if FFT layout is tileable across the specified batch layout.
    """
    return _contiguous_layout(sorted_batch_shape, sorted_batch_strides)

def axis_order_in_memory(strides):
    """
    Compute the order in which the axes appear in memory.
    """
    if len(strides) == 0:
        return tuple()

    _, axis_order = zip(*sorted(zip(strides, range(len(strides)))))

    return axis_order

def calculate_strides(shape, axis_order):
    """
    Calculate the strides for the provided shape and axis order.
    """
    strides = [None] * len(shape)

    stride = 1
    for axis in axis_order:
        strides[axis] = stride
        stride *= shape[axis]

    return strides

@dataclass
class MMTraits:
    """An internal data class for capturing the matrix multiplication traits. The
       result traits are captured separately, because we need to wait for the
       epilog to be provided.
    """
    M : int = None
    N : int = None
    K : int = None
    d_mm_shape : Sequence[int] = None
    a_layout_traits : object = None
    b_layout_traits : object = None
    c_layout_traits : object = None
    batch_count : int = None
    batch_shape : Sequence[int] = None
    batch_strides : Sequence[int] = None
    batch_axis_order: Sequence[int] = None

@dataclass
class ResultTraits:
    """An internal data class for capturing the result matrix's traits.
    """
    d_layout_traits : object = None
    result_shape : Sequence[int] = None
    result_strides : Sequence[int] = None

@dataclass
class MatrixLayout:
    """An internal data class for capturing the tensor layout.
    """
    shape : Sequence[int] = None
    strides : Sequence[int] = None
    is_conjugate : bool = None    # Used to support is_conjugate via conjugate_transpose.

@dataclass
class LayoutTraits:
    """An internal data class for capturing the matrix multiplication traits.
    """
    order : int = None            # cublaslt.Order.{ROW, COL}
    ld : int = None
    batch_offset : int = None     # Based on strides
    is_conjugate : bool = None    # Used to support is_conjugate via conjugate_transpose.

def get_matrix_layout_traits(mm_shape, mm_strides, batch_strides):
    # TODO: log errors. Check a and b for 0 strides?
    M, N = mm_shape

    # We also need to handle broadcast dimensions with zero-stride for the c matrix.
    # Important: start with the last dimension to account for cases like (M, 1) : (1, 1) in CuTe notation.
    if mm_strides[1] == 1:
        order = cublaslt.Order.ROW
        ld = mm_strides[0]
        assert ld == 0 or ld >= N, "Internal error."
        batch_offset =  ld * M
    elif mm_strides[0] == 1:
        order = cublaslt.Order.COL
        ld = mm_strides[1]
        assert ld == 0 or ld >= M, "Internal error."
        batch_offset =  ld * N
    else:
        raise ValueError("Unsupported layout.")

    # Batch dimensions should be contiguous in memory, which we have already checked.
    # The batch_offset should be based on the lowest stride in the batch dimension to account for embedded matrices.
    batch_offset = min(batch_strides) if batch_strides else batch_offset

    return order, ld, batch_offset

def get_mm_traits(a_layout, b_layout, c_layout, logger):
    """
    REQUIREMENTS:
        The a and b layouts must correspond to last two axis transposed if the `is_conjugate` qualifier is set. This is
        because cublaslt has only conjugate_transpose, not just conjugate.

        How will this affect 1-D A or B? Depending on where they have the conjugate qualifier or not, it will
        determine whether we prefix or suffix the 1 extent.

    First check A and B compatibility:
    1. Check MM compatibility (K):
        a. First pad A and/or B MM dimensions if 1-D according to NumPy convention.
        b. The padding is used to determine M, N, and K but should not appear in the output dimensions.
        c. If both A and B are N-D, the dimensions must match.
    2. Check batch dimensions:
        a. One of A or B can have missing batch extents, in which case it is broadcast, otherwise
        b. A and B must have the same batch extents and strides.
        c. In addition, the batch dimensions must be tileable (contiguous in memory).

    C can be None. If C is passed in, it must be a vector or matrix. Batching rule is the same as above.
    """
    # TODO: distinguish names between  the input/output (which include the batch dimensions) and the library A, B, C, D operands, which don't.

    a_shape, a_strides = list(a_layout.shape), list(a_layout.strides)
    b_shape, b_strides = list(b_layout.shape), list(b_layout.strides)

    a_batch_shape, a_mm_shape = a_shape[:-2], a_shape[-2:]
    b_batch_shape, b_mm_shape = b_shape[:-2], b_shape[-2:]

    a_batch_strides, a_mm_strides = a_strides[:-2], a_strides[-2:]
    b_batch_strides, b_mm_strides = b_strides[:-2], b_strides[-2:]

    d_mm_shape = []
    if len(a_mm_shape) == 1:
        s, d = a_mm_shape[0], a_mm_strides[0]
        a_mm_shape = [1] + a_mm_shape
        a_mm_strides = [s * d] + a_mm_strides
    else:
        d_mm_shape.append(a_mm_shape[0])    # The first mode for d applies only when a is not a vector.

    if len(b_mm_shape) == 1:
        s, d = b_mm_shape[0], b_mm_strides[0]
        b_mm_shape = b_mm_shape + [1]
        b_mm_strides = b_mm_strides + [s * d]
    else:
        d_mm_shape.append(b_mm_shape[1])    # The second mode for d applies only when b is not a vector.

    logger.debug(f"The MM shape for operand A is {a_mm_shape} with strides {a_mm_strides}.")
    logger.debug(f"The MM shape for operand B is {b_mm_shape} with strides {b_mm_strides}.")
    logger.debug(f"The MM shape for operand D is {d_mm_shape}.")

    # Workarounds for is_conjugate flag, since cuBLASLt currently supports only conjugate_transpose, not conjugate.
    if a_layout.is_conjugate:
        a_mm_shape.reverse()
    if b_layout.is_conjugate:
        b_mm_shape.reverse()
    if c_layout is not None:
        assert not c_layout.is_conjugate, "Internal error."   # Conjugate-transpose cannot be specified for c currently.

    M0, K0 = a_mm_shape
    K1, N0 = b_mm_shape
    if K0 != K1:
        raise ValueError(f"The 'K' extent must match for the operands: K={K0} in operand A is not equal to K={K1} in operand B.")

    if len(a_batch_shape) > 0 and len(b_batch_shape) == 0:
        if a_batch_shape != b_batch_shape:
            raise ValueError(f"The batch dimensions of operands A {a_batch_shape} and B {b_batch_shape} must match.")
        if a_batch_strides != b_batch_strides:
            raise ValueError(f"The batch strides of operands A {a_batch_strides} and B {b_batch_strides} must match.")

    batch_shape, batch_strides = a_batch_shape, a_batch_strides
    logger.debug(f"The batch shape is {batch_shape} with strides {batch_strides}.")

    # Check batch is tileable.
    if len(batch_shape) > 0:
        sorted_batch_shape, sorted_batch_strides = zip(*sorted(((batch_shape[a], batch_strides[a]) for a in range(len(batch_shape))), key=lambda v: v[-1]))
        if not check_batch_tileable(sorted_batch_shape, sorted_batch_strides):
            message = f"The batch layout corresponding to shape = {batch_shape} and strides = {batch_strides} is currently not supported because it is not tileable."
            #TODO: create custom exception.
            raise ValueError(message)
        logger.debug(f"The batch layout corresponding to shape = {batch_shape} and strides = {batch_strides} IS tileable.")

    batch_count = functools.reduce(operator.mul, batch_shape, 1)

    # Determine the batch axis order.
    batch_axis_order = axis_order_in_memory(batch_strides)

    # Create matrix layout traits.
    a_order, a_ld, a_batch_offset = get_matrix_layout_traits(a_mm_shape, a_mm_strides, a_batch_strides)
    a_layout_traits = LayoutTraits(order=a_order, ld=a_ld, batch_offset=a_batch_offset, is_conjugate=a_layout.is_conjugate)
    logger.debug(f"The layout order for operand A is {a_order.name}, with LD {a_ld}, and batch offset {a_batch_offset}.")

    b_order, b_ld, b_batch_offset = get_matrix_layout_traits(b_mm_shape, b_mm_strides, b_batch_strides)
    b_layout_traits = LayoutTraits(order=b_order, ld=b_ld, batch_offset=b_batch_offset, is_conjugate=b_layout.is_conjugate)
    logger.debug(f"The layout order for operand B is {b_order.name}, with LD {b_ld}, and batch offset {b_batch_offset}.")

    # Process matrix c, if provided.
    c_layout_traits = None
    if c_layout is not None:
        # C can be a vector of dimension M, which is broadcast.
        # C can be a matrix of dimension (M, N) or (M, 1), broadcast in the latter case and has to have contiguous strides.
        # C can be batched matrices of dimension (..., M, N) or (..., M, 1), broadcast in the latter case and has to have contiguous strides.
        c_shape, c_strides = list(c_layout.shape), list(c_layout.strides)

        c_batch_shape, c_mm_shape = c_shape[:-2], c_shape[-2:]
        c_batch_strides, c_mm_strides = c_strides[:-2], c_strides[-2:]
        if len(c_mm_shape) == 1:
            s, d = c_mm_shape[0], c_mm_strides[0]
            c_mm_shape = c_mm_shape + [1]
            c_mm_strides = c_mm_strides + [s * d]
        logger.debug(f"The MM shape for operand C is {c_mm_shape} with strides {c_mm_strides}.")

        Mc, Nc = c_mm_shape
        if Mc != M0:
            # TODO: log errors.
            raise ValueError(f"The M dimension of the c matrix ({Mc}) must match the M dimension of a.")

        if Nc != 1 and Nc != N0:
            # TODO: log errors.
            raise ValueError(f"The N dimension of the c matrix ({Nc}) must match the N dimension of b.")

        if c_batch_shape != batch_shape:
            raise ValueError(f"The batch dimension of operand C {c_batch_shape} must match with that of the other operands {batch_shape}.")
        if c_batch_strides != batch_strides:
            raise ValueError(f"The batch strides of operand C {c_batch_strides} must match with that of the other operands {batch_strides}.")

        c_order, c_ld, c_batch_offset = get_matrix_layout_traits(c_mm_shape, c_mm_strides, c_batch_strides)
        c_layout_traits = LayoutTraits(order=c_order, ld=c_ld, batch_offset=c_batch_offset, is_conjugate=c_layout.is_conjugate)
        logger.debug(f"The layout order for operand C is {c_order.name}, with LD {c_ld}, and batch offset {c_batch_offset}.")

    return MMTraits(M=M0, N=N0, K=K0, d_mm_shape=d_mm_shape, batch_count=batch_count, batch_shape=batch_shape, batch_strides=batch_strides, batch_axis_order=batch_axis_order,
                    a_layout_traits=a_layout_traits, b_layout_traits=b_layout_traits, c_layout_traits=c_layout_traits)

def get_result_traits(mm_traits, epilog_ordering, logger):
    """
    epilog_order = value of type cublaslt.Order

    The result layout is determined from:
    - the epilog requirement, if it exists, or
    - the ordering of operands c, if it is provided, or
    - the ordering of operand a.

    The result batch dimensions must have the same extents and axis order as the inputs. The MM layout can be C or F.
    """
    # The result shape is the batch shape + d_mm_shape.
    result_shape = mm_traits.batch_shape + mm_traits.d_mm_shape

    if epilog_ordering is not None:
        result_ordering = epilog_ordering
    elif mm_traits.c_layout_traits is not None:
        result_ordering = mm_traits.c_layout_traits.order
    else:
        result_ordering = mm_traits.a_layout_traits.order

    if result_ordering == cublaslt.Order.ROW:
        d_order = list(range(len(mm_traits.d_mm_shape) - 1, -1, -1))
    elif result_ordering == cublaslt.Order.COL:
        d_order = list(range(len(mm_traits.d_mm_shape)))
    else:
        assert False, "Internal Error."

    result_axis_order = [len(mm_traits.d_mm_shape) + a for a in mm_traits.batch_axis_order] + d_order

    # Calculate the result strides.
    result_strides = calculate_strides(result_shape, result_axis_order)

    # The result's traits.
    d_batch_strides, d_mm_strides = result_strides[:len(mm_traits.batch_shape)], result_strides[len(mm_traits.batch_shape):]
    d_order, d_ld, d_batch_offset = get_matrix_layout_traits(mm_traits.d_mm_shape, d_mm_strides, d_batch_strides)
    d_layout_traits = LayoutTraits(order=d_order, ld=d_ld, batch_offset=d_batch_offset, is_conjugate=False)
    logger.debug(f"The layout order for operand D is {d_order.name}, with LD {d_ld}, and batch offset {d_batch_offset}.")

    return ResultTraits(result_shape=result_shape, result_strides=result_strides, d_layout_traits=d_layout_traits)

class InvalidMatmulState(Exception):
    pass

class Matmul:
    """
    Matmul(a, b, /, c=None, *, alpha=None, beta=None, scale=None, qualifiers=None, options=None, stream=None)

    Create an object encapsulating the specified matrix multiplication computation and the required resources. A stateful object allows for
     management of a set of related resources in an intuitive, *performant*, and *safe* manner. The resources include workspace memory and operand references
    as well as library objects such as handles that are used internally in the implementation. The implementation and APIs ensure that the
    internal and external resources needed for an operation remain valid, and the resources are released when no longer needed. In other
    words, the APIs make it impossible to use a resource that is no longer available.

    A stateful object can be used to amortize the cost of preparation (planning in the case of matrix multiplication) across multiple executions (also see the
    `StatefulObjects` section).

    In general, all stateful APIs in nvmath-python are based on the same design pattern with the following key phases:

    1. The first phase is *problem specification*, which captures the definition of the operation, together with options that influence the
       behavior of the operation. This phase is as light-weight as possible, and essentially ensures that the problem is well-defined and
       is currently supported by the implementation.
    2. The next phase is _preparation_. In the case of matrix multiplication, this involves planning to determine the best algorithmic implementation
       to use for this specific definition. An optional autotuning operation also falls within the preparation phase. The preparation phase is
       typically relatively expensive, and can depend on user-provided options for planning and autotuning.
    3. The final phase is _execution_. The execution can be repeated multiple times (with the operands being modified in-place using the features
       provided by the operand package, or explicitly reset using :meth:`reset_operand` API). The cost of the first two phases is amortized
       across the multiple executions.

    The function-form API :func:`matmul` is a convenient alternative to using stateful objects for *single* use (the user needs to perform just one
    matrix multiplication, for example), in which case there is no possibility of amortizing preparatory costs. The function-form APIs are just convenience
    wrappers around the stateful object APIs.

    Additional information on what's happening in the various phases described above can be obtained by passing in a :class:`logging.Logger` object
    to :class:`FFTOptions` or by setting the appropriate options in the root logger object, which is used by default:

        >>> import logging
        >>> logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M:%S')

    A user can select the desired logging level and, in general, take advantage of all of the functionality offered by the Python `logging` module.

    Args:
        * TODO *
        stream: Provide the CUDA stream to use for Matmul construction, which is needed for stream-ordered operations such as allocating memory. Acceptable
            inputs include ``cudaStream_t`` (as Python :class:`int`), :class:`cupy.cuda.Stream`, and :class:`torch.cuda.Stream`. If a stream is not provided,
            the current stream from the operand package will be used. As a general note, since a stream is an execution-ordering construct, it is associated
            with individual _operations_ instead of being bound to the object _state_.

    See Also:
    """

    def __init__(self, a, b, /, c=None, *, alpha=None, beta=None, scale=None, qualifiers=None, options=None, stream=None):
        # Check consistency of shapes, strides, batch, data type, etc.
        # Get the scale type as the max precision and corresponding compute type.
        # If c is provided, beta cannot be None. Default alpha is 1., and beta is 0.
        ...
        options = utils.check_or_create_options(configuration.MatmulOptions, options, "Matrix multiplication options")
        self.options = options

        self.logger = options.logger if options.logger is not None else logging.getLogger()

        # TODO: see if it's better to have a list of 2 or 3 operands instead of a, b, c.
        self.a = tensor_wrapper.wrap_operand(a)
        self.b = tensor_wrapper.wrap_operand(b)
        self.logger.info(f"= SPECIFICATION PHASE =")
        self.logger.info(f"The data type of operand A is '{self.a.dtype}', and that of operand B is '{self.b.dtype}'.")
        if c is None:
            self.c = None
        else:
            self.c = tensor_wrapper.wrap_operand(c)
            self.logger.info(f"The data type of operand C is {self.c.dtype}.")

        if self.c is not None and beta is None:
            raise ValueError("A value for beta must be provided if matrix c is provided.")

        if self.a.dtype != self.b.dtype:
            raise ValueError(f"The dtype of operands A {self.a.dtype} and B {self.b.dtype} must be the same.")
        self.ab_dtype_name = self.a.dtype

        # TODO: First look at qualifiers and decide whether to transpose each operand (if it's not a vector).

        # Infer the library package & device ID the operands belong to.
        operands = [self.a, self.b]
        if self.c is not None:
            operands.append(self.c)
        self.operands = operands

        self.package = utils.get_operands_package(operands)
        self.memory_space = 'cuda'
        self.device_id = utils.get_operands_device_id(operands)
        if self.device_id is None:
            if self.package == 'numpy':
                self.package = 'cupy'
            self.memory_space = 'cpu'
            self.device_id = options.device_id
        self.logger.info(f"The input operands' memory space is {self.memory_space}, and the execution space is on device {self.device_id}.")

        # Allocate device memory (in stream context) if needed.
        stream_holder = utils.get_or_create_stream(self.device_id, stream, self.package)
        self.logger.info(f"The specified stream for the Matmul ctor is {stream_holder.obj}.")

        # Copy operands to device if needed.
        # TODO: clear up self.operands vs self.a, self.b, self.c.
        if self.memory_space == 'cpu':
            self.operands = tensor_wrapper.to(self.operands, self.device_id, stream_holder)

        # Set blocking or non-blocking behavior.
        self.blocking = self.options.blocking is True or self.memory_space == 'cpu'
        if self.blocking:
            self.call_prologue = "This call is blocking and will return only after the operation is complete."
        else:
            self.call_prologue = "This call is non-blocking and will return immediately after the operation is launched on the device."

        # The result class is that of the first wrapped device operand.
        self.result_class = self.operands[0].__class__

        self.device = cp.cuda.Device(self.device_id)

        # Set memory allocator.
        self.allocator = options.allocator if options.allocator is not None else memory._MEMORY_MANAGER[self.package](self.device_id, self.logger)

        # Set memory limit.
        self.memory_limit = utils.get_memory_limit(self.options.memory_limit, self.device)
        self.logger.info(f"The memory limit is {formatters.MemoryStr(self.memory_limit)}.")

        # Set handle. We don't destroy handles we create.
        if options.handle is not None:
            self.handle = options.handle
        else:
            self.handle = get_handle(self.device_id)

        # Determine the scale type.
        if options.scale_type is None:
            self.scale_type      = NAME_TO_DEFAULT_SCALE_TYPE[self.ab_dtype_name]
            self.scale_type_name = typemaps.DATA_TYPE_TO_NAME[self.scale_type]
        else:
            self.scale_type = options.scale_type
            if self.scale_type not in typemaps.DATA_TYPE_TO_NAME:
                message = f"Unsupported scale type. The data type '{self.scale_type}' is currently not supported."
                raise ValueError(message)
            self.scale_type_name = typemaps.DATA_TYPE_TO_NAME[self.scale_type]
        self.logger.info(f"The scale type is '{self.scale_type_name}'.")

        # Determine the data types for a and b.
        self.a_dtype = typemaps.NAME_TO_DATA_TYPE[self.a.dtype]
        self.b_dtype = typemaps.NAME_TO_DATA_TYPE[self.b.dtype]

        # Determine the data type for c (if not provided) and d. The two must match.
        if self.c is None:
            self.d_dtype_name, self.d_dtype = self.ab_dtype_name, typemaps.NAME_TO_DATA_TYPE[self.ab_dtype_name]
            self.c_dtype = self.d_dtype
        else:
            self.c_dtype = typemaps.NAME_TO_DATA_TYPE[self.c.dtype]
            self.d_dtype = self.c_dtype
            self.d_dtype_name = typemaps.DATA_TYPE_TO_NAME[self.d_dtype]
        self.logger.info(f"The data type for the result D is '{self.d_dtype_name}'.")

        # Determine the compute type.
        self.compute_type = options.compute_type if options.compute_type is not None else SCALE_TYPE_TO_COMPUTE_TYPE[self.scale_type]
        if self.compute_type not in cublas.ComputeType:
            message = f"Unsupported compute type. The compute type '{self.compute_type}' is currently not supported."
            raise ValueError(message)
        self.logger.info(f"The compute type is {self.compute_type.name}.")

        #TODO: need to generalize alpha and beta for (batched) host or device vectors.
        assert isinstance(alpha, (int, float, type(None))) and isinstance(beta, (int, float, type(None))), "Unsupported alpha or beta type."
        self.alpha = np.zeros((1,), dtype=self.scale_type_name)
        self.alpha[0] = alpha if alpha is not None else 1

        self.beta = np.zeros((1,), dtype=self.scale_type_name)
        self.beta[0] = beta if beta is not None else 0

        # Create operand layouts.
        a_layout = MatrixLayout(self.a.shape, self.a.strides)
        b_layout = MatrixLayout(self.b.shape, self.b.strides)
        c_layout = MatrixLayout(self.c.shape, self.c.strides) if self.c is not None else self.c

        # Get the operation traits.
        self.mm_traits     = get_mm_traits(a_layout, b_layout, c_layout, self.logger)
        self.result_traits = None    # Wait till planning to determine this based on the epilog.
        self.logger.info(f"The matrix multiplication attributes are M = {self.mm_traits.M}, N = {self.mm_traits.N}, and K = {self.mm_traits.K}.")
        self.logger.info(f"The batch count is {self.mm_traits.batch_count}, and the batch shape is {self.mm_traits.batch_shape} with batch strides {self.mm_traits.batch_strides}.")

        # Create and set the operation descriptor.
        self.mm_desc = cublaslt.matmul_desc_create(self.compute_type, self.scale_type)

        mm_desc_ifc = matmul_desc_ifc.MatmulDescInterface(self.mm_desc)
        mm_desc_ifc.compute_type    = self.compute_type
        mm_desc_ifc.scale_type      = self.scale_type
        mm_desc_ifc.sm_count_target = options.sm_count_target
        mm_desc_ifc.fast_accum      = options.fast_accumulation
        self.logger.info(f"The SM count target is {options.sm_count_target}.")
        self.logger.info(f"The flag for fast accumulation mode is {options.fast_accumulation}.")

        # TODO: set alpha and beta pointer modes once device vector support is implemented.

        # TODO: set transpose mode for A and B only for is_conjugate.

        # TODO: set FP8 scale.

        # Epilog attributes: name-to-operand.
        self.epilog_operands = dict()

        # Plan attributes.
        self.preference_ptr  = None
        self.a_layout_ptr, self.b_layout_ptr, self.c_layout_ptr, self.d_layout_ptr = None, None, None, None
        self.flop_count = 0
        self.mm_planned = False

        # Algorithm attributes.
        self.algorithms_buffer = None
        self.algorithm_objects = None

        # Workspace attributes.
        self.workspace_ptr, self.workspace_size = None, None
        self.workspace_allocated_here = False

        # Attributes to establish stream ordering.
        self.workspace_stream = None
        self.last_compute_event = None

        self.valid_state = True
        self.logger.info("The Matmul operation has been created.")

    #TODO: need to add preconditions.
    def applicable_algorithm_ids(self, limit=8):
        ...
        # AlgoGetIDs - depends only on types not on epilogue. If limit is None, all applicable algorithm IDs will be returned.
        algo_ids = cublaslt.matmul_algo_get_ids(self.handle, self.compute_type, self.scale_type, self.a_dtype, self.b_dtype, self.c_dtype, self.d_dtype, limit)
        return algo_ids

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.free()

    def _check_valid_matmul(self, *args, **kwargs):
        """
        Check if the Matmul object is alive and well.
        """
        if not self.valid_state:
            raise InvalidMatmulState("The Matmul object cannot be used after resources are free'd")

    def _free_plan_resources(self, exception=None):
        """
        Free resources allocated in planning.
        """

        # Destroy matrix layouts.
        if self.a_layout_ptr is not None:
            cublaslt.matrix_layout_destroy(self.a_layout_ptr)
            self.a_layout_ptr = None
        if self.b_layout_ptr is not None:
            cublaslt.matrix_layout_destroy(self.b_layout_ptr)
            self.b_layout_ptr = None
        if self.c is not None:   # Note that c layout aliases with that of d.
            cublaslt.matrix_layout_destroy(self.c_layout_ptr)
        self.c_layout_ptr = None
        if self.d_layout_ptr is not None:
            cublaslt.matrix_layout_destroy(self.d_layout_ptr)
            self.d_layout_ptr = None

        if self.preference_ptr is not None:
            cublaslt.matmul_preference_destroy(self.preference_ptr)
            self.preference_ptr = None

        self.mm_planned   = False
        return True

    #TODO: need to add preconditions.
    def plan(self, *, preferences=None, algorithm_ids=None, epilog=None, epilog_inputs=None, stream=None): # Epilog inputs require as many inputs (with specific shapes etc) as required by the epilogue. It's either a tensor or a sequence of tensors.
        """
        """
        self.logger.info(f"= PLANNING PHASE =")

        # TODO: if algorithm_ids is not None, filter by it.
        # TODO: get algorithms as well, users can pickle algorithms and provide them later. Change option name to algorithms to accept both?

        # Clear epilog operands, since different epilogs can be provided in different calls.
        # We don't need to worry about ordering, since it's the user's responsibility to order calls that accept a stream argument.
        # This applies to CPU operands as well even though we move them to the GPU since the execution is blocking.
        # TODO: reuse epilog operands if allocated on the CPU, so we can remove this?
        self.epilog_operands = dict()

        mm_traits = self.mm_traits
        mm_desc_ifc = matmul_desc_ifc.MatmulDescInterface(self.mm_desc)

        stream_holder = utils.get_or_create_stream(self.device_id, stream, self.package)
        self.logger.info(f"The specified stream for the matrix multiplication plan is {stream_holder.obj}.")

        # Base FLOP count.
        self.flop_count = 2 * mm_traits.M * mm_traits.N * mm_traits.K
        self.logger.info(f"The base matrix multiplication FLOP count is {formatters.FLOPSStr(self.flop_count, 'FLOP')}.")

        # TODO: move epilog processing to separate function?
        epilog_ordering = None
        if epilog is not None:
            # TODO: support all epilogs.
            assert epilog in EPILOG_HANDLERS_MAP, "Not supported."
            self.logger.info(f"The specified epilog is {epilog.name}.")

            # Add epilog FLOP count to base value.
            self.flop_count += EPILOG_FLOP_COUNT_MAP[epilog](mm_traits.M, mm_traits.N)
            self.logger.info(f"The total FLOP count (including epilog) is {formatters.FLOPSStr(self.flop_count, 'FLOP')}.")

            epilog_handler_types = EPILOG_HANDLERS_MAP[epilog]
            if epilog_handler_types:
                epilog_handlers = [handler_type(self.logger, mm_traits, epilog) for handler_type in epilog_handler_types]

                # Check if the epilog requires a specific result layout, and if the requirement is consistent for all the handlers.
                epilog_handlers_ordering = set(h.order for h in epilog_handlers)
                assert len(epilog_handlers_ordering) == 1, "Internal error."
                epilog_ordering = epilog_handlers_ordering.pop()

                required_epilog_input_names = set(h.name for h in epilog_handlers)

                self.logger.info(f"The epilog requires the following additional inputs: {required_epilog_input_names}.")
                if required_epilog_input_names and epilog_inputs is None:
                    raise ValueError(f"The epilog {epilog.name} requires the following input tensors: {required_epilog_input_names}.")

                if required_epilog_input_names != set(epilog_inputs.keys()):
                    raise ValueError(f"The epilog {epilog.name} requires the following input tensors: {required_epilog_input_names}. The provided tensor names are: {epilog_inputs.keys()}")

                # Wrap epilog inputs. Take a copy of the user-provided dict.
                epilog_inputs = epilog_inputs.copy()
                for name in epilog_inputs:
                    epilog_inputs[name] = tensor_wrapper.wrap_operand(epilog_inputs[name])

                # Check if epilog inputs all belong to the same package, which is the same as the package of the MM operands.
                epilog_package = utils.get_operands_package(list(epilog_inputs.values()))   # TODO: avoid list() ctor.
                epilog_package = 'cupy' if epilog_package == 'numpy' else epilog_package   # Handle the NumPy <=> CuPy asymmetry.
                if self.package != epilog_package:
                    message = f"Library package mismatch for epilog: '{self.package}' => '{epilgue_package}'"
                    raise TypeError(message)

                # Check if all epilog inputs all are on the same device, which is the device of the operands.
                device_id = utils.get_operands_device_id(list(epilog_inputs.values()))    # TODO: avoid list() ctor.
                if self.device_id != device_id:
                    raise ValueError(f"The epilog inputs must be on the same device ({device_id}) as the operands ({self.device_id}).")

                # First validate all epilog inputs. This is to avoid unnecessary copy to the GPU in case some inputs are not valid.
                for handler in epilog_handlers:
                    handler.validate(epilog_inputs[handler.name])

                # Move epilog inputs to the GPU, if needed.
                if device_id is None:
                    for e in required_epilog_input_names:
                        self.logger.debug(f"The epilog input {e} will be copied to device{self.device_id}.")
                        self.epilog_operands[e] = tensor_wrapper.to(epilog_inputs[e], self.device_id, stream_holder)
                else:
                    for e in required_epilog_input_names:
                        self.epilog_operands[e] = epilog_inputs[e]

                # Finally, update the MM descriptor. Note that we pass in self.epilog_operands (which are on the GPU).
                for handler in epilog_handlers:
                    handler.update(mm_desc_ifc, self.epilog_operands[handler.name])

            # Set the epilog. At this point, we're sure that the epilog inputs, if any, are valid and have been set.
            mm_desc_ifc.epilogue = epilog

        # Fill the result traits, now that we know the epilog.
        self.result_traits = result_traits = get_result_traits(mm_traits, epilog_ordering, self.logger)
        self.logger.info(f"The layout order for the result D is {self.result_traits.d_layout_traits.order.name}, with LD {self.result_traits.d_layout_traits.ld}, and batch offset {self.result_traits.d_layout_traits.batch_offset}.")

        preferences = utils.check_or_create_options(configuration.MatmulPreferences, preferences, "Matrix multiplication plan preferences")

        # TODO: fix M and K for qualifier is_conjugate == True.
        self.a_layout_ptr = cublaslt.matrix_layout_create(self.a_dtype, rows=mm_traits.M, cols=mm_traits.K, ld=mm_traits.a_layout_traits.ld)
        self.b_layout_ptr = cublaslt.matrix_layout_create(self.b_dtype, rows=mm_traits.K, cols=mm_traits.N, ld=mm_traits.b_layout_traits.ld)
        self.d_layout_ptr = cublaslt.matrix_layout_create(self.d_dtype, rows=mm_traits.M, cols=mm_traits.N, ld=result_traits.d_layout_traits.ld)

        layout_a_ifc = matrix_layout_ifc.MatrixLayoutInterface(self.a_layout_ptr)
        layout_a_ifc.order = mm_traits.a_layout_traits.order
        layout_a_ifc.batch_count = mm_traits.batch_count
        layout_a_ifc.strided_batch_offset = mm_traits.a_layout_traits.batch_offset

        layout_b_ifc = matrix_layout_ifc.MatrixLayoutInterface(self.b_layout_ptr)
        layout_b_ifc.order = mm_traits.b_layout_traits.order
        layout_b_ifc.batch_count = mm_traits.batch_count
        layout_b_ifc.strided_batch_offset = mm_traits.b_layout_traits.batch_offset

        layout_d_ifc = matrix_layout_ifc.MatrixLayoutInterface(self.d_layout_ptr)
        layout_d_ifc.order = result_traits.d_layout_traits.order
        layout_d_ifc.batch_count = mm_traits.batch_count
        layout_d_ifc.strided_batch_offset = result_traits.d_layout_traits.batch_offset

        if self.c is None:
            self.c_layout_ptr = self.d_layout_ptr
        else:
            self.c_layout_ptr = cublaslt.matrix_layout_create(self.c_dtype, rows=mm_traits.M, cols=mm_traits.N, ld=mm_traits.c_layout_traits.ld)
            layout_c_ifc = matrix_layout_ifc.MatrixLayoutInterface(self.c_layout_ptr)
            layout_c_ifc.order = mm_traits.c_layout_traits.order
            layout_c_ifc.batch_count = mm_traits.batch_count
            layout_c_ifc.strided_batch_offset = mm_traits.c_layout_traits.batch_offset

        limit = preferences.limit
        num_algorithms = np.empty((1,), dtype=np.int32)
        self.algorithms_buffer  = np.zeros((limit,), dtype=algorithm.algorithm_dtype)

        # TODO: the semantics of the following is cumulative with multiple calls to planning, is it what we want?
        if self.preference_ptr is None:
            self.preference_ptr = cublaslt.matmul_preference_create()

        # Set preferences.
        preference_ifc = matmul_pref_ifc.MatmulPreferenceInterface(self.preference_ptr)
        preference_ifc.max_workspace_bytes = self.memory_limit
        preference_ifc.reduction_scheme_mask = preferences.reduction_scheme_mask
        preference_ifc.max_waves_count = preferences.max_waves_count
        preference_ifc.impl_mask = preferences.numerical_impl_mask

        # Set minimum aligments.
        # TODO: clean up self.operands vs self.a, self.b, self.c.
        a_ptr, b_ptr = self.operands[0].data_ptr, self.operands[1].data_ptr
        preference_ifc.min_alignment_a_bytes = min(256, pointer_aligned_to(a_ptr))
        preference_ifc.min_alignment_b_bytes = min(256, pointer_aligned_to(b_ptr))
        self.logger.debug(f"The minimum alignment for operand A is {preference_ifc.min_alignment_a_bytes} bytes.")
        self.logger.debug(f"The minimum alignment for operand B is {preference_ifc.min_alignment_b_bytes} bytes.")
        if self.c is not None:
            c_ptr = self.operands[2].data_ptr
            preference_ifc.min_alignment_c_bytes = min(256, pointer_aligned_to(c_ptr))
            self.logger.debug(f"The minimum alignment for operand C is {preference_ifc.min_alignment_c_bytes} bytes.")
        # The result alignment should be 256 bytes.
        self.logger.debug(f"The minimum alignment for the result D is the default 256 bytes.")

        # TODO: limit search by algo IDs.

        timing =  bool(self.logger and self.logger.handlers)
        self.logger.info("Starting matrix multiplication planning...")
        with utils.device_ctx(self.device_id), utils.cuda_call_ctx(stream_holder, blocking=True, timing=timing) as (self.last_compute_event, elapsed):
            cublaslt.matmul_algo_get_heuristic(self.handle, self.mm_desc, self.a_layout_ptr, self.b_layout_ptr, self.c_layout_ptr, self.d_layout_ptr, self.preference_ptr, limit, self.algorithms_buffer.ctypes.data, num_algorithms.ctypes.data)

        num_algorithms = num_algorithms[0]
        if num_algorithms == 0:
            raise RuntimeError("Planning failed to find any suitable algorithm.")
        self.algorithms_buffer = self.algorithms_buffer[:num_algorithms]

        # Create algorithm objects.
        self.algorithm_objects = tuple(algorithm.Algorithm(a) for a in self.algorithms_buffer)

        # Create the map from object to buffer.
        self.algorithm_object_to_buffer = dict(zip(self.algorithm_objects, self.algorithms_buffer))

        # TODO: check why the cast to int is needed - float is returned otherwise.
        self.workspace_size = int(np.max(self.algorithms_buffer["workspace_size"]))

        self.logger.info(f"The plan found {num_algorithms} suitable algorithms within the requested limit of {limit} algorithms, with a workspace requirement of {formatters.MemoryStr(self.workspace_size)}.")

        self.mm_planned = True
        if elapsed.data is not None:
            self.logger.info(f"The matrix multiplication planning phase took {elapsed.data:.3f} ms to complete.")

        return self.algorithm_objects

    @property
    def algorithms(self):
        # Get sequence of algorithm objects, inquire their capabilities, and configure.
        return self.algorithm_objects

    #TODO: need to add preconditions.
    def reset(self, *operands, alpha=None, beta=None, scale=None, epilog_inputs=None, stream=None):
        """
        Two or three operands, consistent with what was provided, or (None,). If None is provide, all kwargs should also be None.
        Split resetting operands from resetting alpha, beta, and scale into two methods? Otherwise it will be all or none for reset.
        """
        # TODO
        ...

    #TODO: need to add preconditions.
    def autotune(self, iterations=3, prune=None, release_workspace=False, stream=None): # Prune means keep top N of the algorithms only.
        self.logger.info(f"= AUTOTUNING PHASE =")
        # For now use cupyx.profiler.benchmark
        from cupyx.profiler import benchmark
        # Measure time taken for autotuning.
        from timeit import default_timer as timer

        self.logger.info(f"Starting autotuning...")
        start = timer()

        num_algorithms = len(self.algorithm_objects)
        limit = prune if prune is not None else num_algorithms
        self.logger.info(f"The number of algorithms in the plan is {num_algorithms}, from which the top {limit} will be retained.")
        self.logger.info(f"The requested number of iterations is {iterations}.")

        # Autotune setup.
        # TODO: try to factor out common setup between autotune and execute.
        stream_holder = utils.get_or_create_stream(self.device_id, stream, self.package)

        # Allocate workspace if needed.
        self._allocate_workspace_memory_perhaps(stream_holder)

        # TODO: need to create empty tensors for auxiliary output.
        # Create empty tensor for the result.
        result = utils.create_empty_tensor(self.result_class, self.result_traits.result_shape, self.d_dtype_name, self.device_id, stream_holder, self.result_traits.result_strides)
        result_ptr = result.data_ptr

        c_ptr = self.operands[2].data_ptr if self.c is not None else result_ptr
        a, b = self.operands[0], self.operands[1]
        raw_workspace_ptr = utils.get_ptr_from_memory_pointer(self.workspace_ptr)
        alpha_ptr, a_ptr, b_ptr, beta_ptr = self.alpha.ctypes.data, self.a.data_ptr, self.b.data_ptr, self.beta.ctypes.data

        def execute_matmul(algorithm_ptr):
            cublaslt.matmul(self.handle, self.mm_desc, alpha_ptr, a_ptr, self.a_layout_ptr, b_ptr, self.b_layout_ptr, beta_ptr, c_ptr, self.c_layout_ptr, result_ptr, self.d_layout_ptr, algorithm_ptr, raw_workspace_ptr, self.workspace_size, stream_holder.ptr)

        # Tune.
        with utils.device_ctx(self.device_id), utils.cuda_call_ctx(stream_holder, blocking=False, timing=False) as (self.last_compute_event, elapsed):
            gpu_times = list()
            for algorithm_struct in self.algorithms_buffer:
                algorithm_ptr = algorithm_struct['algorithm'].ctypes.data
                t = list()
                for i in range(iterations):
                   start0 = stream_holder.obj.record()
                   #t = benchmark(execute_matmul, kwargs={'algorithm_ptr': algorithm_ptr}, n_repeat=iterations)
                   execute_matmul(algorithm_ptr=algorithm_ptr)
                   end0 = stream_holder.obj.record()
                   end0.synchronize()
                   t.append(cp.cuda.get_elapsed_time(start0, end0))
                # Convert the GPU time from seconds to milliseconds below.
                #gpu_times.append(1000. * cp.min(t.gpu_times))    # TODO: use min or mean?
                gpu_times.append(min(t))    # TODO: use min or mean?

        # Establish ordering wrt the computation and free workspace if it's more than the specified cache limit.
        self._release_workspace_memory_perhaps(release_workspace=release_workspace)
        self._reset_workspace_allocation_tracking()

        # Get the sort order based on the GPU times.
        sorted_gpu_times, sort_order = zip(*sorted(zip(gpu_times, range(num_algorithms))))

        # Reorder the algorithms buffer according to the sort order, and prune it.
        algorithms_buffer  = np.zeros((limit,), dtype=algorithm.algorithm_dtype)
        for i in range(limit):
            algorithms_buffer[i]  = self.algorithms_buffer[sort_order[i]]
        self.algorithms_buffer  = algorithms_buffer

        # Create algorithm objects.
        self.algorithm_objects = tuple(algorithm.Algorithm(a) for a in self.algorithms_buffer)

        # Create the map from object to buffer.
        self.algorithm_object_to_buffer = dict(zip(self.algorithm_objects, self.algorithms_buffer))

        gpu_times_str = ", ".join(f"{t:0.3f}" for t in gpu_times)
        self.logger.info(f"The autotuned GPU times (in milliseconds) are: {gpu_times_str}.")
        self.logger.info(f"The corresponding sort order is: {sort_order}.")
        orig_flop_rate = self.flop_count / gpu_times[0] * 1000
        if sort_order[0] != 0:
            self.logger.info(f"Autotuning found that the algorithm originally ranked {sort_order[0]} is the best out of the {num_algorithms} in the plan, and moved it to rank 0.")
            new_flop_rate = self.flop_count / sorted_gpu_times[0] * 1000
            self.logger.info(f"Autotuning has improved performance from {formatters.FLOPSStr(orig_flop_rate, 'FLOP/s')} to {formatters.FLOPSStr(new_flop_rate, 'FLOP/s')}.")
        else:
            self.logger.info(f"Autotuning found that the algorithm ranked best by the plan heuristics remains the best out of the {num_algorithms} algorithms in the plan.")
            self.logger.info(f"The best performance remains at {formatters.FLOPSStr(orig_flop_rate, 'FLOP/s')}.")

        end = timer()
        self.logger.info(f"The autotuning took {(end - start) * 1000.:.3f} ms to complete.")

    def _check_planned(self, *args, **kwargs):
        what = kwargs['what']
        if not self.mm_planned:
            raise RuntimeError(f"{what} cannot be performed before plan() has been called.")

    def _check_valid_operands(self, *args, **kwargs):
        raise NotImplementedError("TODO")

    #TODO: need to add preconditions.
    def _allocate_workspace_memory_perhaps(self, stream_holder):
        """
        Allocate workspace memory using the specified allocator, if it hasn't already been done.
        """

        if self.workspace_ptr is not None:
            return

        assert self.workspace_size is not None, "Internal Error."
        assert self.workspace_allocated_here is False, "Internal Error."

        self.logger.debug(f"Allocating workspace for performing the matrix multiplication...")
        with utils.device_ctx(self.device_id), stream_holder.ctx:
            try:
                self.workspace_ptr = self.allocator.memalloc(self.workspace_size)
            except TypeError as e:
                message = "The method 'memalloc' in the allocator object must conform to the interface in the "\
                          "'BaseCUDAMemoryManager' protocol."
                raise TypeError(message) from e
            raw_workspace_ptr = utils.get_ptr_from_memory_pointer(self.workspace_ptr)

        self.workspace_stream = stream_holder.obj
        self.logger.debug(f"Finished allocating device workspace of size {formatters.MemoryStr(self.workspace_size)} in the context of stream {self.workspace_stream}.")

    def _free_workspace_memory(self, exception=None):
        """
        Free workspace by releasing the MemoryPointer object.
        """
        if self.workspace_ptr is None:
            return True

        self.workspace_ptr = None
        self.logger.debug("[_free_workspace_memory] The workspace has been released.")

        return True

    def _reset_workspace_allocation_tracking(self):
        """
        Reset workspace allocation tracking attributes to False at the end of the methods where workspace memory is
        potentially allocated. This is necessary to prevent any exceptions raised before method entry from using
        stale tracking values.
        """
        self.workspace_allocated_here = False


    #TODO: need to add preconditions.
    def _release_workspace_memory_perhaps(self, release_workspace):
        """
        Free workspace memory if it's larger than the specified limit.
        """
        if not release_workspace:
            return True

        # Establish ordering wrt the computation and free workspace if it's more than the specified cache limit.
        if self.last_compute_event is not None:
            self.workspace_stream.wait_event(self.last_compute_event)
            self.logger.debug("Established ordering with respect to the computation before releasing the workspace.")

        self.logger.debug("[_release_workspace_memory_perhaps] The workspace memory will be released.")
        self._free_workspace_memory()

    def _release_workspace_memory_perhaps_wrapper(self, exception=None):
        """
        This is used in @atomic.
        """
        self._release_workspace_memory_perhaps(release_workspace=self.workspace_allocated_here)
        return True

    #TODO: need to add preconditions.
    def execute(self, *, algorithm_object=None, alpha=None, beta=None, release_workspace=False, stream=None):   # Only scalar values of alpha and beta allowed here.
        self.logger.info(f"= EXECUTION PHASE =")
        stream_holder = utils.get_or_create_stream(self.device_id, stream, self.package)
        self.logger.info(f"The specified stream for execute() is {stream_holder.obj}.")

        # Allocate workspace if needed.
        self._allocate_workspace_memory_perhaps(stream_holder)

        # TODO: need to create empty tensors for auxiliary output.
        # Create empty tensor for the result.
        self.logger.debug("Beginning output (empty) tensor creation...")
        self.logger.debug(f"The output tensor shape = {self.result_traits.result_shape} with strides = {self.result_traits.result_strides} and data type '{self.d_dtype_name}'.")
        self.result = utils.create_empty_tensor(self.result_class, self.result_traits.result_shape, self.d_dtype_name, self.device_id, stream_holder, self.result_traits.result_strides)
        self.logger.debug("The output (empty) tensor has been created.")

        result_ptr = self.result.data_ptr

        # Select the first (best) algorithm if one is not provided.
        if algorithm_object is None:
            algorithm_struct = self.algorithms_buffer[0]['algorithm']
            self.logger.info(f"The highest ranked algorithm in the plan (algorithm id = {self.algorithm_objects[0].algorithm_id}) will be used.")
        else:
            assert isinstance(algorithm_object, algorithm.Algorithm), "Invalid algorithm object."
            algorithm_struct = self.algorithm_object_to_buffer[algorithm_object]['algorithm']
            self.logger.info(f"The specified algorithm object (algorithm id = {algorithm_object.algorithm_id}) will be used.")

        c_ptr = self.operands[2].data_ptr if self.c is not None else self.result.data_ptr
        a, b = self.operands[0], self.operands[1]
        raw_workspace_ptr = utils.get_ptr_from_memory_pointer(self.workspace_ptr)
        timing =  bool(self.logger and self.logger.handlers)
        self.logger.info(f"Starting matrix multiplication...")
        self.logger.info(f"{self.call_prologue}")
        with utils.device_ctx(self.device_id), utils.cuda_call_ctx(stream_holder, self.blocking, timing) as (self.last_compute_event, elapsed):
            cublaslt.matmul(self.handle, self.mm_desc, self.alpha.ctypes.data, self.a.data_ptr, self.a_layout_ptr, self.b.data_ptr, self.b_layout_ptr, self.beta.ctypes.data, c_ptr, self.c_layout_ptr, self.result.data_ptr, self.d_layout_ptr, algorithm_struct.ctypes.data, raw_workspace_ptr, self.workspace_size, stream_holder.ptr)

        if elapsed.data is not None:
            self.logger.info(f"The matrix multiplication calculation took {elapsed.data:.3f} ms to complete.")

        # Establish ordering wrt the computation and free workspace if it's more than the specified cache limit.
        self._release_workspace_memory_perhaps(release_workspace=release_workspace)

        # Return the result.
        if self.memory_space == 'cpu':
            out = self.result.to('cpu', stream_holder=stream_holder)
        else:
            out = self.result.tensor

        # Release internal reference to the result to permit recycling of memory.
        self.result = None
        self._reset_workspace_allocation_tracking()

        return out

    def free(self):
        """Free Matmul resources.

        It is recommended that the :class:`Matmul` object be used within a context, but if it is not possible then this
        method must be called explicitly to ensure that the matrix multiplication resources (especially internal library objects) are
        properly cleaned up.
        """

        if not self.valid_state:
            return

        try:
            # Future operations on the workspace stream should be ordered after the computation.
            if self.last_compute_event is not None:
                self.workspace_stream.wait_event(self.last_compute_event)

            self._free_workspace_memory()

            self._free_plan_resources()

            # We won't destroy the handle.

        except Exception as e:
            self.logger.critical("Internal error: only part of the Matmul object's resources have been released.")
            self.logger.critical(str(e))
            raise e
        finally:
            self.valid_state = False

        self.logger.info("The Matmul object's resources have been released.")


# TODO: add algorithm_ids and possibly algorithm.
def matmul(a, b, /, c=None, *, alpha=None, beta=None, scale=None, epilog=None, epilog_inputs=None, qualifiers=None, options=None, preferences=None, stream=None):

    # Set algorithm limit to 1, but take a copy first if needed.
    if isinstance(preferences, configuration.MatmulPreferences):
        preferences = copy.copy(preferences)

    preferences = utils.check_or_create_options(configuration.MatmulPreferences, preferences, "Matrix multiplication plan preferences")
    preferences.limit = 1

    with Matmul(a, b, c=c, alpha=alpha, beta=beta, scale=scale, options=options, stream=stream) as mm:

        mm.plan(preferences=preferences, epilog=epilog, epilog_inputs=epilog_inputs, stream=stream)

        r = mm.execute(stream=stream)

    return r
