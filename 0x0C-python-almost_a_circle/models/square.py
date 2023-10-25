#!/usr/bin/python3
'''
Module: 10. And now, the Square! to 12. Square update
class square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class square that inherits from class rextangle '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initialisation of class object
         Args:
            size (int): The size of the new Square.
            x (int): x coordinate of the new Square.
            y (int): y coordinate of the new Square.
            id (int):id the new Square.
'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return (self.width)

    @size.setter
    def size(self, value):
        ''' setter for size '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    def __str__(self):
        ''' returns the print and str representation of a square'''
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        '''
        sets the artributes: id, width, height, x and y via args or kwargs
        '''
        if args:
            for index, value in enumerate(args, start=1):
                if index == 1:
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                if index == 2:
                    self.size = value
                if index == 3:
                    self.x = value
                if index == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                if kwargs["id"] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation wof a square"""

        dict_rep = {}

        dict_rep["id"] = self.id
        dict_rep["size"] = self.size
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y

        return (dict_rep)
