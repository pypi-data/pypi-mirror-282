# Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# SPDX-License-Identifier: Apache-2.0

__all__ = ['MatrixStructure', 'MatrixStructureCOL32', 'MatrixStructureCOL4_4R2_8C', 'MatrixStructureCOL32_2R_4R4', 'MatrixStructureDenseStrided']

# TODO: Add Banded, Symmetric, Triangular, etc. Should we capture packing via name or attribute?

from abc import ABC, abstractmethod

import numpy as _np

class MatrixStructure(ABC):

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def structure(self):
        """The structure of the data: triangular, symmetric, banded, ...."""
        raise NotImplementedError

    @property
    @abstractmethod
    def format(self):
        """The format of the data: packed or full."""
        raise NotImplementedError

class MatrixStructureDenseStrided(MatrixStructure):
    """
    The default matrix structure for Matmul.
    """

    @property
    def name(self):
        return "DENSE_STRIDED"

class MatrixStructureCOL32(MatrixStructure):
    """
    The matrix should be in column-major layout.
    """

    @property
    def name(self):
        return "COL32"


class MatrixStructureCOL4_4R2_8C(MatrixStructure):
    """
    The matrix should be in column-major layout.
    """

    @property
    def name(self):
        return "COL4_4R2_8C"

class MatrixStructureCOL32_2R_4R4(MatrixStructure):
    """
    The matrix should be in column-major layout.
    """

    @property
    def name(self):
        return "COL32_2R_4R4"
