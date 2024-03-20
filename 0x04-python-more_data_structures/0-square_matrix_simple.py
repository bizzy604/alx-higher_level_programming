#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r_matrix = []
    for row in matrix:
        tmp = []
        for item in row:
            tmp.append(item ** 2)
        r_matrix.append(list(tmp))
        tmp.clear()
    return (r_matrix)
