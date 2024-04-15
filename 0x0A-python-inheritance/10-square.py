#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py):"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Initialising object"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method for square"""
        return self.__size ** 2

    def __str__(self):
        """str representation"""
        return f"[Rectangle] {self.__size}/{self.__size}"
