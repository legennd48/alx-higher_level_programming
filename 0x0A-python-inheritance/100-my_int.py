#!/usr/bin/python3
"""
Module: 12. My integer
class MyInt that inherits from int:
"""


class MyInt(int):
    '''inherits from int'''
    def __eq__(self, other):
        """
        Override the equality operator (==) to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to invert its behavior.
        """
        return super().__eq__(other)
