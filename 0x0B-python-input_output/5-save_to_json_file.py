#!/usr/bin/python3
"""
A module for a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes 'my_obj' to 'filename'.
    Args:
        my_obj (str): JSON representation
        filename (str): filename to be created
    """
    with open(filename, "w", encoding="utf-8") as js:
        json.dump(my_obj, js)
