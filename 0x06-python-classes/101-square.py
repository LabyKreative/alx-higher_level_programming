#!/usr/bin/python3

'''Defines a class of square'''


class Square:
    '''Square functions come in here'''

    def __init__(self, size=0, position=(0, 0)):
        '''Square function get initialised'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Sets the current position of square'''
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Returns the current area of square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''Prints the square with the # character'''
        if self.__size == 0:
            print('')
            return

        [print('') for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            print('')

    def __str__(self):
        '''Prints function representation of square'''
        if self.__size != 0:
            [print('') for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(' ', end='') for y in range(0, self.__position[0])]
            [print('#', end='') for z in range(0, self.__size)]
            if x != self.__size - 1:
                print('')
        return ('')
