#!/usr/bin/python3
"""
Module: 1. My list
class MyList that inherits from list
"""


class MyList(list):
    """Type class MyList with print_sorted function"""

    def print_sorted(self):
        '''prints sorted list of ints'''
        sorted_list = sorted(self)
        print(sorted_list)
