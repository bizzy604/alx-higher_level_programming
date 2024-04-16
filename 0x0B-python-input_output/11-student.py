#!/usr/bin/python3
"""
Module for a class Student that defines a student
(based on 10-student.py)
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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of Student instance
        """
        dct = {}
        if (isinstance(attrs, list) and
                all(isinstance(element, str) for element in attrs)):
            for keys in attrs:
                for item, value in self.__dict__.items():
                    if item is keys:
                        dct[keys] = value
            return dct
        else:
            for key, value in self.__dict__.items():
                if (isinstance(value, (list, dict, str, int, bool))):
                    dct[key] = value
            return dct

    def reload_from_json(self, json):
        """Replaces all attributes of the class instance.
        Args:
            json (dict) : dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
