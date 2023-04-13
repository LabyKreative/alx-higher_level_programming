#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """This reprsents the base geometry"""

    def area(self):
        """Not implement yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Parameter validation as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
