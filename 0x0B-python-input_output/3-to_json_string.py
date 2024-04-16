#!/usr/bin/python3
"""
A module for a function that returns the JSON representation
of an object (string)
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj.
    Args:
        my_obj (object): object to be represented as json
    Return:
        JSON repesentaiton of my_obj
    """
    return json.dumps(my_obj)
