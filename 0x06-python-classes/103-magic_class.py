#!/usr/bin/python3
''' code to match provided bytecode '''
import math


class MagicClass:
    ''' class definition '''
    def __init__(self, radius=0):
        ''' initialization of rad'''
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        ''' returns area '''
        return (2 * math.pi * self.__radius ** 2)

    def circumference(self):
        ''' calculates circumference '''
        return (2 * math.pi * self.__radius)
