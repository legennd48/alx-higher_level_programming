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
