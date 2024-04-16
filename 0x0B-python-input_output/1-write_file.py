#!/usr/bin/python3
"""A module for a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Write a string(text) to textfile(filename).
    Args:
        filename (str): filename to be created
        text (str): text to be inserted to file
    Return:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as wf:
        return (wf.write(text))
