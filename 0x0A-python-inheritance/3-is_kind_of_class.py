#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """This checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if the object is an instance of, or if the object is an isntance
        of a class inherited from, the specified class; 
        otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
