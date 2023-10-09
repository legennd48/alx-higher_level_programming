#!/usr/bin/python3
"""
Module: 3. is_kind_of_class
Returns True if the object is an instance of the specified class or a subclass;
otherwise, False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class or its subclass.

    Args:
        obj: Object to be checked.
        a_class: Class to compare with the object.

    Returns:
        True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
