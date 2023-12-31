#!/usr/bin/python3
"""
Module: 8-rectangle
Contains parent class BaseGeometry with public
instance method area and integer_validator

Contains subclass Rectangle with instantiation of private
attributes _width and _height, validated by parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass Rectangle inherits from BaseGeometry.

    Attributes:
        _width (int): Width of the rectangle (private).
        _height (int): Height of the rectangle (private).
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        Raises:
            TypeError, ValueError.
        """
        super().integer_validator("width", width)
        self._width = width
        super().integer_validator("height", height)
        self._height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """

        return self._width * self._height
