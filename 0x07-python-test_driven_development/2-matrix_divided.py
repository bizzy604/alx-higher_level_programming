#!/bin/usr/python3
""" Module for a function that divides a matrix
matrix must be a matrix (list of lists) of integers/floats and same size
div must be a number (integer or float)
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """Function to divide all elements of a matrix
    Args:
        matrix (list): Matrix (list of list)
        div (int): Number to divide matrix with
    Return:
        New matrix with divided elements
    """
    n_matrix = list()

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    try:
        len_1 = len(matrix[0])
    except Exception:
        TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if (len(matrix) < 2):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if (len(matrix[1]) < len_1):
        raise TypeError(
                "Each row of the matrix must have the same size")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if (len(row) < len_1):
            raise TypeError("Each row of the matrix must have the same size")

        tmp = list()
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            tmp.append(round((item / div), 2))
        n_matrix.append(tmp)

    return (n_matrix)
