#!/usr/bin/python3
'''Find max integer in a list'''


def max_integer(list=[]):
    '''Find and return the max integer in a list of integers
        the function returns None
    '''
    if len(list) == 0:
        return None
    result = list[0]
    x = 1
    while x < len(list):
        if list[x] > result:
            result = list[x]
        x += 1
    return result
