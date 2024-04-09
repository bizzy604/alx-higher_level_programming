#!/usr/bin/python3
"""Continuation module for a function that defines a Rectangle"""


class Rectangle:
    """Class that defines a rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intitialising objects
        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """ String represantation of instance"""
        if (self.__width == 0 or self.__height == 0):
            return ""
        else:
            if (isinstance(Rectangle.print_symbol, list) is True):
                for row in range(self.__height):
                    tmp = []
                    for elem in range(self.__width):
                        tmp.append(elem)
                    print(tmp)
                return ""
            for row in range(self.__height):
                count = 0
                while (count < self.__width):
                    print(self.print_symbol, end="")
                    count += 1
                if (row != self.height - 1):
                    print("")
        return ""

    def __repr__(self):
        """ repr() of instance"""
        str_1 = "Rectangle(" + str(self.__width)
        str_1 += ", " + str(self.__height) + ")"
        return (str_1)

    def __del__(self):
        """Action to do when del (deleting) instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on Area.
        Args:
            rect_1 (instance of Rectangle): rectangle 1
            rect_2 (instance of Rectangle): rectangle 2
        Return:
            biggest rectangle by area
            rect_1 if both have same area value
        """
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if (area_1 == area_2):
            return rect_1
        elif (area_1 > area_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns Rectangle instance with width == height == size
        Args:
            size (int): size of rectangle
        """
        new = cls(width=size, height=size)
        return (new)
