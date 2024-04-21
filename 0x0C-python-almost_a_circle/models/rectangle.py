#!/usr/bin/python3
"""
Module for Class 'Rectangle' that inherits from Class 'Base'.
"""
from models.base import Base


class Rectangle(Base):
    """
    Class inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing Rectangle object.
        Args:
            width (int) : width of Rectangle
            height (int) : height of Rectangle
            x (int) : default = 0
            y (int) : default = 0
            id (int) : default = 0
        """
        super().__init__(id)
        if (isinstance(width, int) is False):
            raise TypeError("width must be an integer")
        if (isinstance(height, int) is False):
            raise TypeError("height must be an integer")
        if (isinstance(x, int) is False):
            raise TypeError("x must be an integer")
        if (isinstance(y, int) is False):
            raise TypeError("y must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if (height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if (x < 0):
            raise ValueError("x must be >= 0")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter and setter fot width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter and setter fot height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter and setter fot x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter and setter fot y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns area of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the char '#'
        """
        y_count = 0
        while (y_count < self.__y):
            print("")
            y_count += 1
        for row in range(0, self.__height):
            count = 0
            x_count = 0
            while (x_count < self.__x):
                print(" ", end="")
                x_count += 1
            while (count < self.__width):
                print("#", end="")
                count += 1
            print("")

    def __str__(self):
        """
        Str representation
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        for updating attributes
        Args:
            args[0] : id
            args[1] : width
            args[2] : height
            args[3] : x
            args[4] : y
        """
        if (len(args) < 1):
            if ("id" in kwargs.keys()):
                self.id = kwargs["id"]
            if ("width" in kwargs.keys()):
                self.__width = kwargs["width"]
            if ("height" in kwargs.keys()):
                self.__height = kwargs["height"]
            if ("x" in kwargs.keys()):
                self.__x = kwargs["x"]
            if ("y" in kwargs.keys()):
                self.__y = kwargs["y"]
        else:
            args_c = len(args)
            if (args_c == 1):
                self.id = args[0]
            elif (args_c == 2):
                self.id = args[0]
                self.__width = args[1]
            elif (args_c == 3):
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif (args_c == 4):
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            elif (args_c >= 5):
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]

    def to_dictionary(self):
        """
        returns dictionary representation of object
        """
        obj_dict = {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
        return obj_dict
