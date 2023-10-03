#!/usr/bin/python3

'''
Module: 1-rectangle.py
a class that defines a rectangle
'''


class Rectangle:
    '''Class defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''initialize the rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        ''' Width Getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Sets the value for width '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Height Getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Sets the value for height '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Return the area of rectangle'''
        area = self.__width * self.__height
        return (area)

    def perimeter(self):
        '''that returns the rectangle perimeter'''

        if (self.__width == 0 or self.__height == 0):
            perimeter = 0
        else:
            perimeter = (self.__height * 2) + (self.__width * 2)
        return (perimeter)

    def __str__(self):
        ''' Returns printable representation of rextangle using '#' '''
        if self.__width == 0 or self.__height == 0:
            return ('')
        rect = []
        for i in range(self.__height):
            [rect.append('#') for m in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return (''.join(rect))
