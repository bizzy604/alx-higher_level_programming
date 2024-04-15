#!/usr/bin/python3
"""Module for a a class MyList that inherits from list"""


class MyList(list):
    """class that inherits from 'list'"""
    def print_sorted(self):
        """function that prints the list, sorted (ascending sort)"""
        print(sorted(self))
