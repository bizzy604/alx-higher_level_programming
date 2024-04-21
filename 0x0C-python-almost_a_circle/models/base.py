#!/usr/bin/python3
"""
Module to define Class 'Base'
"""
import json


class Base:
    """
    Base class for all other classes for this peoject.
    Attributes:
        __nb_objects (int) : number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing object.
        Args:
            id (int) : object id
        """
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON str representation of list_dictionaries
        Args:
            list_dictionaries(dict): List of dictionaries
        Return:
            JSON string
        """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation of list_objs to a file
        Args:
            list_objs(list): list of instances who inherits from base
        """
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = "{}.json".format(class_name)
        list_dictionaries = []
        for obj in list_objs:
            dictionary_representation = obj.to_dictionary()
            list_dictionaries.append(dictionary_representation)
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        Args:
            json_string(str): json string representation
        Return:
            list of JSON str representation
        """
        if json_string is None:
            return []
        str_repr = json.loads(json_string)
        return str_repr

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        Args:
            dictionary(kwargs)
        """
        if "size" not in dictionary.keys():
            inst = cls(width=dictionary["width"], height=dictionary["height"])
            inst.update(**dictionary)
        else:
            inst = cls(size=dictionary["size"])
            inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        classname = cls.__name__
        filename = "{}.json".format(classname)
        instance_list = []
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list
