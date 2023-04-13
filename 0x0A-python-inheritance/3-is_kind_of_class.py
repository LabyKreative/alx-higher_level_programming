#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """This checks if an object is an instance of,
    or inherited instance of a class that inherited from,
    the specified class.
    """
    if isinstance(obj, a_class):
        return True
    return False
