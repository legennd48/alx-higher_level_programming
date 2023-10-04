#!/usr/bin/python3
"""
Modulee: lazy_matrix multiplication
performs multiplication of matrix using numpy lib

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the result
    """
    return (np.matmul(m_a, m_b))
