#!/usr/bin/python3
'''
Module: 2. Say my name
prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):

    '''
    prints My name is <first name> <last name>
    '''

    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string".
                        format("first_name" if isinstance(last_name, str)
                               else "last_name"))
