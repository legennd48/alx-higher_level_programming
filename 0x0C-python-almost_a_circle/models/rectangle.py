#!/usr/bin/python3
'''
Module: 2. First Rectangle
 class Rectangle that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    ''' A rectangle class that inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' intial definition of Rectangle class
        Args:
            width (int): width of rect
            height (int): Height of Rectangle
            x (int):
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter (Rectangle)."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x coordinate getter """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y coordinate getter."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' Clalculates the area of the Rectangle '''
        return (self.height * self.width)

    def display(self):
        ''' Displays a pictorial rep of the rectangle using # '''
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for h in range(self.__height)))

    def __str__(self):
        ''' overiding str mothod to display message'''

        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''
        Assignes new values to the attribute id, width, height, x and y
        This change may be done via args or kwargs
        '''
        if args:
            for index, value in enumerate(args, start=1):
                if index == 1:
                    self.id = value
                elif index == 2:
                    self.width = value
                elif index == 3:
                    self.height = value
                elif index == 4:
                    self.x = value
                else:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle'''
        newDic = {"id": self.id, "width": self.width, "height": self.height,
                  "x": self.x, "y": self.y}
        return (newDic)
