#!/usr/bin/python3
"""A module for a function that checks available attributes and
methods of an object
"""


def lookup(obj):
    """Fucntion that returns list of available attr and methodsof object
    Args:
        obje (list): object to be checked
    """
    lst = dir(obj)
    return lst
