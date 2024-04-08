#!/bin/usr/python3
"""Module for a function that prints a full name
Takes first and last names
Both must be strings
"""


def say_my_name(first_name, last_name=""):
    """A function that prints full name
    Args:
        first_name (str): First name string
        last_name (str): Last name string
    Return:
        None
    """
    if (isinstance(first_name, str) is False):
        raise TypeError("first_name must be a string")
    if (isinstance(last_name, str) is False):
        raise TypeError("last_name must be a string")

    for char in first_name:
        try:
            random = float(char)
        except Exception:
            pass
        else:
            raise TypeError("first_name must be a string")

    for char2 in last_name:
        try:
            random = float(char2)
        except Exception:
            pass
        else:
            raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
