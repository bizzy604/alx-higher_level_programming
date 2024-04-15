#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from 7-base_geometry Module"""
    def __init__(self, width, height):
        """Initialising object"""
        if (self.integer_validator("width", width)):
            self.__width = width
        if (self.integer_validator("height", height)):
            self.__height = height
