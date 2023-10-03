#!/usr/bin/python3
'''
module: add_integer
Afunction that adds two integers
'''


def add_integer(a, b=98):
    '''
    Adds 2 integers and return the result
    Raise: TypeError
    '''

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
