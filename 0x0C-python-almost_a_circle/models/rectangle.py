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
        """Returns a string representation of the rectangle."""
        display_str = ""
        for _ in range(self.y):
            display_str += "\n"
        for _ in range(self.height):
            display_str += " " * self.x + "#" * self.width + "\n"
        return display_str


    def __str__(self):
        ''' overiding str mothod to display message'''

        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                setattr(self, attributes[idx], value)
        else:
            for key, value in kwargs.items():
                if key in ["id", "width", "height", "x", "y"]:
                    if key == "width" and not isinstance(value, int):
                        raise TypeError("width must be an integer")
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle'''
        newDic = {"id": self.id, "width": self.width, "height": self.height,
                  "x": self.x, "y": self.y}
        return (newDic)
