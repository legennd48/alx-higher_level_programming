#!/usr/bin/python3
"""
Module: 100-matrix_mul
Does matrix multiplication on two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Does matrix multiplication and
    Returns the result of matrix multiplication
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

    if not all((isinstance(item, (int, float)))
               for item in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(item, (int, float)))
               for item in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    reverse_matrix = []
    for i in range(len(m_b[0])):
        new_row = []
        for j in range(len(m_b)):
            new_row.append(m_b[j][i])
        reverse_matrix.append(new_row)

    result = []
    for row_a in m_a:
        new_row = []
        for col_b in reverse_matrix:
            temp_sum = 0
            for idx in range(len(reverse_matrix[0])):
                temp_sum += row_a[idx] * col_b[idx]
            new_row.append(temp_sum)
        result.append(new_row)

    return (result)
