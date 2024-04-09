#!/usr/bin/python3
"""Continuation module for a function that defines a Rectangle"""


class Rectangle:
    """Class that defines a rectangle object"""
    def __init__(self, width=0, height=0):
        """Intitialising objects
        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter and setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle parameter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ""
        else:
            for row in range(self.__height):
                for elem in range(self.__width):
                    print("#", end="")
                if (row != self.height - 1):
                    print("")
        return ""

    def __repr__(self):
        str_1 = "Rectangle(" + str(self.__width)
        str_1 += ", " + str(self.__height) + ")"
        return (str_1)
