#!/usr/bin/python3
"""
Module: 12. Pascal's Triangle
Returns a list of integer lists representing Pascal's triangle of a given size
"""


def generate_pascals_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): Number of rows to generate.

    Returns:
        List[List[int]]: A list of integer lists representing Pascal's triangle.
    """
    triangle = [[1]]  # Initialize with the first row
    while len(triangle) != n:
        last_row = triangle[-1]
        new_row = [1]  # First element of every row is 1
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)  # Last element of every row is 1
        triangle.append(new_row)
    return triangle
