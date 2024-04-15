#!/usr/bin/python3
"""a function that returns True if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly
        an instance of the specified class
    Args:
        obj (object): object to be checked
        a_class (class): class to be compared to
    Return:
        True if obj is instance of a_class
        else Retrun False
    """
    if (type(obj) == a_class):
        return True
    return False
