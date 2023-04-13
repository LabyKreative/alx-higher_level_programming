#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """This represent a student"""

    def __init__(self, first_name, last_name, age):
        """This initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This retrieves a dictionary representation of the Student"""
        if (type(attrs) == list and
                all(type(st) == str for st in attrs)):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}
        return self.__dict__

    def reload_from_json(self, json):
        """This replaces all attributes of the Student"""
        for y, z in json.items():
            setattr(self, y, z)
