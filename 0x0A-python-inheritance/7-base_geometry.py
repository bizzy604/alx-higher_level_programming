#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """class that defines area function"""
    def area(self):
        """Function to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value'.
        Args:
            name (str)
            value (int)
        """
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
