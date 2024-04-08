#!/usr/bin/python3
"""Module for a function that prints a formated text
Prototype: def text_indentation(text)
'text' must be a string, otherwise raise a TypeError raised
"""


def text_indentation(text):
    """Function that prints text to stdout.
    Args:
        text (str): String text to be printed
    """
    if (isinstance(text, str) is False):
        raise TypeError("text must be a string")
    paragraph = ""
    for char in text:
        paragraph += char
        if char in [".", "?", ":"]:
            print(paragraph.strip())
            print("")
            paragraph = ""
    if paragraph:
        print(paragraph.strip(), end="")
