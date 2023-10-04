#!/usr/bin/python3
"""
module: 2-matrix_divided
Defines a matrix division function
"""


def matrix_divided(matrix, div):
    """
    Divide all elements in a matrix
    Args:
    matrix: matrix type arg of list
    div: div type int or float
    Return: new matrix with division calculated
    Raise: TypeError, ZeroDivisionError
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(item, int) or isinstance(item, float))
                for item in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of list"
                        " of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

    return (new)
