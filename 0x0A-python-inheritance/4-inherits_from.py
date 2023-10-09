#!/usr/bin/python3
"""
Module: 4. Only sub class of
returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is inherited from the specified class.

    Args:
        obj: Object to be checked.
        a_class: Class to compare with the object.

    Returns:
        True if obj is inherited from a_class, False otherwise.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
