#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from 7-base_geometry Module"""
    def __init__(self, width, height):
        """Initialising object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
