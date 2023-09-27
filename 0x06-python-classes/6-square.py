#!/usr/bin/python3
''' class square with setter, getter, prints the shape andfinds the  area '''


class Square:
    ''' class defines a square. '''
    def __init__(self, size=0, position=(0, 0)):
        ''' Instantiation of private instance attribute.
        Args:
        param1: size of the square which must be int
        param2:position of new square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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

    def my_print(self):
        ''' prints the square using # '''
        size = self.__size
        if (size == 0):
            print()

        for i in range(size):
            print("#" * size)

    @property
    def position(self):
        ''' retireves current square position '''
        return (self.__position)

    @position.setter
    def position(self, value):
        ''' stes the value of position '''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
