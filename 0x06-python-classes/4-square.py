#!/usr/bin/python3

'''Define a class Square'''


class Square:
    '''Square functions come in here'''

    def __init__(self, size=0):
        '''A new square gets initialised'''
        self.size = size

    @property
    def size(self):
        '''Sets the current size of square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Returns the current area of square'''
        return (self.__size ** 2)
