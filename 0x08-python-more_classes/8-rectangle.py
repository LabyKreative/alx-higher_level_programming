#!/usr/bin/python3
"""Defines a Recangle class"""


class Rectangle:
    """ Init Class width set 0 and height set 0"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate Area """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculate Perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ Rectangle for print """
        recstr = ""
        if self.width == 0 or self.height == 0:
            return recstr
        else:
            sym = self.print_symbol
            for j in range(self.height):
                recstr += "{}".format(sym * self.__width)
                if j != (self.height - 1):
                    recstr += "\n"
        return recstr

    def __repr__(self):
        """ Representation a string """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Action when object is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static Method check area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            rect_2
