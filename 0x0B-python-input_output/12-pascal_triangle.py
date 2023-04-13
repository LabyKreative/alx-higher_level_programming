#!/usr/bin/python3
"""Defines a Pascal triangle function"""


def pascal_triangle(n):
    """This represents Pascal Triangle n.

    Returns an empty list if n <= 0
    """
    lst = []
    if n <= 0:
        return lst
    for x in range(n):
        for y in range(x + 1):
            if y == 0:
                lst.append([1])
            elif y == x:
                lst[x].append(1)
            else:
                lst[x].append(lst[x - 1][y] + lst[x - 1][y - 1])
    return lst
