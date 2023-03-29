#!/usr/bin/python3

'''Defines a class of square.'''


class Square:
    '''Square functions come in here'''

    def __init__(self, size=0):
        '''New square get initialised'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
