#!/usr/bin/python3
'''Defines a Rectangle class'''


class Rectangle:
    '''This class is for manage a rectangle'''

    def __init__(self, width=0, height=0):
        '''Set a objet with width and height'''

        self.height = height
        self.width = width

    @property
    def width(self):
        '''Put width'''

        return self.__width

    @width.setter
    def width(self, value):
        '''set the width in the object'''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Put height'''

        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of the object'''

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
