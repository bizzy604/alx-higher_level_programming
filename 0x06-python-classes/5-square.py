#!/usr/bin/python3
"""Continuation of a module for a class that defines a square"""


class Square():
    """A class that defines a square"""
    def __init__(self, size=0):
        """Initialising square object
        Args:
            size(int): size of sqaure
        """
        self.__size = size

    @property
    def size(self):
        """getter and setter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """"method that return area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """method that prints the square with the character '#'"""
        if (self.__size == 0):
            print("")
        else:
            count = int()
            count2 = int()
            for row in range(0, self.__size):
                for colm in range(0, self.__size):
                    print("#", end="")
                print("")
