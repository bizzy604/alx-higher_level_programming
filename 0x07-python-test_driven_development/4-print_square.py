#!/usr/bin/python3
"""Module for a function that prints a square.
print square with the character #.
uses 'size' to print the number of '#' characters
"""


def print_square(size):
    """A function that prints a Square.
    Args:
        size (int): Size of the square
    Return:
        None
    """
    if (isinstance(size, int) is False):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for row in range(size):
        count = 0
        while (count < size):
            print("#", end="")
            count += 1
        print("")
