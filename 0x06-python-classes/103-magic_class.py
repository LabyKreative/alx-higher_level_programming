#!/usr/bin/python3

'''Defines a MagicClass'''

import math


class MagicClass:
    '''Represents randomness'''

    def __init__(self, radius=0):
        '''Initialises MagicClass radius'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''Calculates the area of MagicClass'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''Returns the circuference of the MagicClass'''
        return 2 * math.pi * self.__radius
