#!/usr/bin/python3
"""Continuation of a module thta defines the class Square"""


class Square():
    """continuation of a class that defines a square"""
    def __init__(self, size=0):
        """Ititializing class object with size.
        Args:
            size of square
        """
        self.__size = size

    @property
    def size(self):
        """Getter and setter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method that returns area of square
        Return:
            Area of square
        """
        return (self.__size ** 2)
