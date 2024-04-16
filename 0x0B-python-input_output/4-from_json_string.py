#!/usr/bin/python3
"""
A module for a function that returns an object,
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns an object represented by JSON string.
    Args:
        my_str (str): JSON string representation
    """
    return json.loads(my_str)
