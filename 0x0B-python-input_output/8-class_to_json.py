#!/usr/bin/python3
"""
A script that return the dictionary description
with simple data structure:
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    Args:
        obj (object): class instance
    """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
