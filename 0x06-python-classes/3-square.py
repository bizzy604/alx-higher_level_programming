#!/usr/bin/python3
"""continuation module for a class that defines a sqaure"""


class Square():
    """a class that defines a square"""
    def __init__(self, size=0):
        """Inititialising class object
        Args:
            size(int): size of square
        """
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method to calculate the area of the square.
        Return:
            Area of the square
        """
        return (self.__size ** 2)
