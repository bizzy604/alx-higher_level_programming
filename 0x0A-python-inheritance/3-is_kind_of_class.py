#!/usr/bin/python3
""" Module for a function that checks instance"""


def is_kind_of_class(obj, a_class):
    """Checks if if the object is an instance of,
        or if the object is an instance of a class
    Args:
        obj (object)
        a_class (class)
    Return:
        True if object is an instance of class
    """
    if (isinstance(obj, a_class)):
        return True
    return False
