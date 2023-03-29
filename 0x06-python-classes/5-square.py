#!/usr/bin/python3

'''Defines a class of square'''


class Square:
    '''Square functions come in here'''

    def __init__(self, size):
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

    def my_print(self):
        '''Print the square with the # character'''
        for x in range(0, self.__size):
            [print('#', end='') for y in range(self.__size)]
            print('')
        if self.__size == 0:
            print('')
