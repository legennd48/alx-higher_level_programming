#!/usr/bin/python3
'''
Module: 10. Square #1
class Square that inherits from Rectangle (9-rectangle.py)
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        __size (int): Size of the square (private).
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
