#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """This represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializez a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        return self.__dict__.copy()
