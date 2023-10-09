#!/usr/bin/python3
"""
Module: 2. Exact same object
Returns True if the object is exactly an instance of the specified class;
otherwise, False.
"""


def is_same_class(obj, a_class):
    """
    Function to check if obj is an instance of the specified class.

    Args:
        obj: Object to be checked.
        a_class: Class to compare with the object.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """

    return type(obj) == a_class
