#!/usr/bin/python3
"""
Module for a function that creates an Object from a 'JSON file'
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.
    Args:
        filename (str): JSON file name to be used
    """
    with open(filename, "r") as jf:
        return json.load(jf)
