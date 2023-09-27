#!/usr/bin/python3
''' class square with setter, getter, prints the shape andfinds the  area '''
import math


class Square:
    '''Class defines a square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Instantiation of private instance attributes.

        Args:
            size (int): Size of the square which must be an integer.
            position (tuple): tuple Position of the square of two integers.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self) -> float:
        '''Returns the current square area.'''
        return float(self.__size ** 2)

    @property
    def size(self) -> int:
        '''Retrieves the current size of the square.'''
        return self.__size

    @size.setter
    def size(self, value: int):
        '''Sets the size of the square.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''Prints the square using #.'''
        size = self.__size
        if size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(size):
            print(" " * self.__position[0] + "#" * size)

    @property
    def position(self) -> tuple:
        '''Retrieves the current square position as a tuple.'''
        return self.__position

    @position.setter
    def position(self, value: tuple):
        '''Sets the position of the square as a tuple of two +ve integers.'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
