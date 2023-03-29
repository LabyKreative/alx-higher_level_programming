#!/usr/bin/python3

'''Defines a class of square'''


class Square:
    '''Square functions come in here'''

    def __init__(self, size=0):
        '''New square gets initialised'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Returns the current area of square'''
        return (self.__size ** 2)

    @property
    def size(self):
        '''Sets the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the square value'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = sizze
