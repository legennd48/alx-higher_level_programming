#!/usr/bin/python3
"""
Defines class Square with private size, position, public area & my_print
while printing to stdout using #
"""


class Square:
    """
    class Square definition
    Args:
        size (int): size of a side in square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        Args:
            size (int): defaults to 0 if none; don't use __size to call setter
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """"
        retrieves and returns size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets new value to size
        Args:
            value: the value to be set
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns area of square
        """
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))

    @property
    def position(self):
        """
        retrieves position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets new value
        Args:
            value: int value to be set
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """
        String representation of square...
        """
        string = ""
        if self.__size == 0:
            return string

        string += "\n" * self.position[1]
        string += "\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)])
        return (string)
