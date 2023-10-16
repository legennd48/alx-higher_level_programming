#!/usr/bin/python3
'''
Module: 2. First Rectangle
 class Rectangle that inherits from Base
'''
import models.base


class Rectangle(Base):
    ''' A rectangle class that inherits from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' intial definition of Rectangle class
        Args:
            width (int): width of rect
            height (int): Height of Rectangle
            x,
            y
            id
        '''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter '''
        return (self.__width)

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be greater than 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return (self.__height)

    @height.setter
    def height(self, value):
        ''' height setter '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be greater than 0")
        else:
            self.__height = value


    @property
    def x(self):
        ''' c0ordinate x getter '''
        return (self.__x)

    @x.setter
    def x(self, value):
        ''' x coordinate setter '''
        if not isinstance(value, int):
            raise TypeError("coordinamte 'x' must be an integer")
        elif value <= 0:
            raise ValueError("coordinate 'x' must be greater than 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' height getter '''
        return (self.__y)

    @y.setter
    def y(self, value):
        ''' coordinate 'y' setter '''
        if not isinstance(value, int):
            raise TypeError("coordinate 'y' must be an integer")
        elif value <= 0:
            raise ValueError("coordinate 'y' must be greater than 0")
        else:
            self.__y = value
