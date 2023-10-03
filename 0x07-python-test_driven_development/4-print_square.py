#!/usr/bin/python3
'''
Module: 3. Print square
prints a square with the character #
'''


def print_square(size):
    '''
    prints a square using '#'
    Args:
    size (int): Size of the Square
    Raises: TypeError, ValueError
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print('', end='')
    else:
        for i in range(size):
            [print('#', end="") for j in range(size)]
            print("")
