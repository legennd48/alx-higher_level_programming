#!/usr/bin/python3
'''
Module: 7. Integer validator
based on 6-base_geometry.py
'''


class BaseGeometry:
    """Type class of BaseGeometry"""

    def area(self):
        """Raises an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is an integer and greater than zero.

        Args:
            name (str): Name of the value being validated.
            value (int): Value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than zero.
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
