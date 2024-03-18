#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for a in r:
            if a is not r[len(r) - 1]:
                print("{:d}".format(a), end=" ")
            else:
                print("{:d}".format(a), end="")
        print()
