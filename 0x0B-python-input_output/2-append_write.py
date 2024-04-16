#!/usr/bin/python3
"""A module for a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Append text(text) to file(filename).
    Args:
        filename (str): filname to be appended/created to.
        text (str): text to be appended
    Return:
        Number of characters printed
    """
    with open(filename, "a+", encoding="utf-8") as af:
        appended = af.write(text)
        return appended
