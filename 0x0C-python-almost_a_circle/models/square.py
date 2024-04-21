#!/usr/bin/python3
"""
Class 'Square' that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Inititializing Square oobject
        Args:
            size (int): size of square
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter and setter for size"""
        return self.__width

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """
        str represantation.
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x,
                                             self.y, self.__width)

    def update(self, *args, **kwargs):
        """
        assigns attributes.
        """
        if (len(args) < 1):
            if ("id" in kwargs.keys()):
                self.id = kwargs["id"]
            if ("size" in kwargs.keys()):
                self.size = kwargs["size"]
                self.__width = kwargs["size"]
                self.__height = kwargs["size"]
            if ("x" in kwargs.keys()):
                self.x = kwargs["x"]
            if ("y" in kwargs.keys()):
                self.y = kwargs["y"]
        else:
            args_c = len(args)
            if (args_c == 1):
                self.id = args[0]
            elif (args_c == 2):
                self.id = args[0]
                self.size = args[1]
                self.__width = args[1]
                self.__height = args[1]
            elif (args_c == 3):
                self.id = args[0]
                self.size = args[1]
                self.__width = args[1]
                self.__height = args[1]
                self.x = args[2]
            elif (args_c >= 4):
                self.id = args[0]
                self.size = args[1]
                self.__width = args[1]
                self.__height = args[1]
                self.x = args[2]
                self.y = args[3]

    def to_dictionary(self):
        """
        returns dict represantation of object.
        """
        obj_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
        return obj_dict
