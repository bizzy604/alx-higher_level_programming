#!/usr/bin/python3
"""
Module for a function that  returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
    - n: Integer representing the number of rows to generate.

    Returns:
    - List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)

        row.append(1)
        triangle.append(row)

    return triangle
