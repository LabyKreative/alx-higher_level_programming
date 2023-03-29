#!/usr/bin/python3

'''Defines a class of square'''


class Square:
    '''Square functions come in here'''

    def __init__(self, size=0):
        '''New square gets initialised'''
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
        return (self.__size * self.__size)

    def __eq__(self, other):
        '''Defines the == comparision to a square'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Defines the != comparison to a square'''
        return self.area() != other.area()

    def __lt__(self, other):
        '''Defines the < comparison to a square'''
        return self.area() < other.area()

    def __le__(self, other):
        '''Define the <= comparison to a square'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''Define the > comparison to a square'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''Defines the >= compmarison to a square'''
        return self.area() >= other.area()
