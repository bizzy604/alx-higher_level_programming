#!/usr/bin/python3
"""A module for a function that reads a text file (UTF8)"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout
    Args:
        filename (str) : filename to be used
    """
    with open(filename, encoding="utf-8") as rf:
        for line in rf:
            print(line, end="")
