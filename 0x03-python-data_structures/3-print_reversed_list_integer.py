#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        max_idx = len(my_list) - 1
        while max_idx >= 0:
            print("{:d}".format(my_list[max_idx]))
            max_idx -= 1
