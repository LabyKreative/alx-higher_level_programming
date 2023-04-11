#!/usr/bin/python3
"""Defines a class, MyList that inherits from list"""


class MyList(list):
    """Implements the built-in sorted printing for class list"""

    def print_sorted(self):
        """This prints a list insorted assending order"""
        print(sorted(self))
