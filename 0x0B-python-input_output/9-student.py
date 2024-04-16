#!/usr/bin/python3
"""
Module for a class Student that defines a student
"""


class Student:
    """
    Defines a a student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Inititializing object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of Student instance
        """
        dct = {}
        for key, value in self.__dict__.items():
            if (isinstance(value, (list, dict, str, int, bool))):
                dct[key] = value
        return dct
