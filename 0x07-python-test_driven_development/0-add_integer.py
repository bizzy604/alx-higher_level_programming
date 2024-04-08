#!/usr/bin/python3
""" Module for a function that adds two integers
This a is testing module for a function that adds two integers
'a' and 'b' must be integers or floats, otherwise raise a TypeError
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """ Fucntion that add two integers.
    Args:
        a (int): first number
        b (int): second number
    Return:
        a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if (isinstance(a, float)):
        a = int(a)
    if (isinstance(b, float)):
        b = int(b)
    return (a + b)
