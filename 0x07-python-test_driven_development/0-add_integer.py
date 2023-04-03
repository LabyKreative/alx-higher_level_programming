#!/usr/bin/python3
'''A function that adds 2 integers'''


def add_integer(a, b=98):
    '''Returns the addition of a and b
    and also he result int datatype.
    Raise TypeError if data is diferrent that int.
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Return the sum of a and b as an integer
    return int(a + b)
