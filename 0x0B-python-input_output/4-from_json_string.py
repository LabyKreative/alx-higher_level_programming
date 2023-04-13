#!/usr/bin/python3
"""Defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """Returns a string Python JSON data representation"""
    return json.loads(my_str)
