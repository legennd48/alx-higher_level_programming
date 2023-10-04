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
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    try:
        np_result = np.matmul(np.array(m_a), np.array(m_b))
        result = np_result.tolist()
        return result
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
