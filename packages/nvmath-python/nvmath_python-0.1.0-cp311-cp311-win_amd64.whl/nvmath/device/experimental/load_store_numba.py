#
# Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES
#
# SPDX-License-Identifier: Apache-2.0
#

from llvmlite import ir
from numba import types
from numba.core import cgutils
from numba.core.extending import intrinsic, overload
from numba.core.typing import signature

# Copy from one array to another (local, shared or global) using as-large-as-possible widths
# Use this as
# fast_copy(input_array, input_index, output_array, output_index)
def make_fast_copy(multiplier):

    @intrinsic
    def f(typingctx, input, input_idx, output, output_idx):

        assert input.dtype.bitwidth == output.dtype.bitwidth
        assert input_idx == output_idx
        sig = signature(types.void, input, input_idx, output, output_idx)

        # sig = void(array<value>, int, array<value>, int)
        def codegen(context, builder, sig, args):

            input_array_type = sig.args[0]
            output_array_type = sig.args[2]
            value_type = input_array_type.dtype
            assert output_array_type.dtype.bitwidth == value_type.bitwidth
            bw = value_type.bitwidth

            input_val, input_idx_val, output_val, output_idx_val = args

            # Get base pointers
            in_ptr = cgutils.create_struct_proxy(input_array_type)(context, builder, input_val).data
            out_ptr = cgutils.create_struct_proxy(output_array_type)(context, builder, output_val).data

            # Offset pointers
            in_ptr = builder.gep(in_ptr, [input_idx_val], inbounds=True)
            out_ptr = builder.gep(out_ptr, [output_idx_val], inbounds=True)

            # max width load/store
            byte_t = ir.IntType(bw * multiplier)
            in_ptr = builder.bitcast(in_ptr, byte_t.as_pointer())
            out_ptr = builder.bitcast(out_ptr, byte_t.as_pointer())

            # Load / store
            val = builder.load(in_ptr)
            builder.store(val, out_ptr)

        return sig, codegen
    
    return f

fast_copy = make_fast_copy(1)
fast_copy_2x = make_fast_copy(2)
fast_copy_4x = make_fast_copy(4)

# Load using maximum width (useful for complex64 or complex128)
# Use this as
# value = load(array, index)
@intrinsic
def load(typingctx, input, input_idx):

    sig = signature(input.dtype, input, input_idx)

    # sig = value(array<value>, int)
    def codegen(context, builder, sig, args):

        array, idx = args
        value_type = context.get_value_type(sig.args[0].dtype)
        bw = sig.args[0].dtype.bitwidth
        byte_t = ir.IntType(bw)

        # Get base pointers + offset it + convert to pointer-to-int
        in_ptr = cgutils.create_struct_proxy(sig.args[0])(context, builder, array).data
        in_ptr = builder.gep(in_ptr, [idx], inbounds=True)
        in_ptr = builder.bitcast(in_ptr, byte_t.as_pointer())

        # Create alloca'd struct of 1 <something> + get pointer to struct
        out_value_ptr = builder.alloca(value_type, size=1, name="fastload")
        out_byte_ptr = builder.bitcast(out_value_ptr, byte_t.as_pointer())

        # Load as an int
        value = builder.load(in_ptr)

        # Store to alloca'd struct as an int
        builder.store(value, out_byte_ptr)

        # Load from alloca'd struct as <something>
        return builder.load(out_value_ptr)

    return sig, codegen

# Store using maximum width (useful for complex64 or complex128)
# Use this as 
# store(value, array, index)
@intrinsic
def store(typingctx, value, output, output_idx):

    assert value == output.dtype
    sig = signature(types.void, value, output, output_idx)

    # sig = void(value, array<value>, int)
    def codegen(context, builder, sig, args):

        value, array, idx = args
        value_type = context.get_value_type(sig.args[1].dtype)
        bw = sig.args[1].dtype.bitwidth
        byte_t = ir.IntType(bw)

        # Get base pointers + offset it + convert to pointer-to-int
        out_ptr = cgutils.create_struct_proxy(sig.args[1])(context, builder, array).data
        out_ptr = builder.gep(out_ptr, [idx], inbounds=True)
        out_ptr = builder.bitcast(out_ptr, byte_t.as_pointer())

        # Create alloca'd struct of 1 <something> + get pointer to struct
        out_value_ptr = builder.alloca(value_type, size=1, name="fastload")
        out_byte_ptr = builder.bitcast(out_value_ptr, byte_t.as_pointer())

        # Store to alloca'd struct
        builder.store(value, out_value_ptr)

        # Load from alloca'd struct as an int
        value = builder.load(out_byte_ptr)

        # Store to out_ptr as an int
        builder.store(value, out_ptr)

    return sig, codegen