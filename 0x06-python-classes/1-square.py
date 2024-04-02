#!/usr/bin/python3
"""amodule that defines a class Square by: (based on 0-square.py)"""


class Square():
    """a class Square that defines a square
    Attributes:
        __size(int): To keep track of the size of the square
    """
    def __init__(self, size):
        """Initializing Square class.
        Args:
            size(int): size of square
        """
        self.__size = size
