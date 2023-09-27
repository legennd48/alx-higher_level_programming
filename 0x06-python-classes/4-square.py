#!/usr/bin/python3
class Square:
    ''' class defines a square. '''
    def __init__(self, size=0):
        ''' Instantiation of private instance attribute.
        Args:
        param1: size of the square which must be int
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' returns the current square area'''
        return (self.__size * self.__size)

    @property
    def size(self):
        ''' retireves current size of square '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' sets size of square '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
