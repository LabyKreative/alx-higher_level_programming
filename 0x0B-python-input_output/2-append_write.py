#!/usr/bin/python3
"""Defines a file appending function"""


def append_write(filename="", text=""):
    """A function that appends a string to the end of a text file(UTF8)
    and returns the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
