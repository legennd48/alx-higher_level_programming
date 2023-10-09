#!/usr/bin/python3
"""
Module: 13. Can I?
adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to the object if possible.

    Args:
        obj: Object to which the attribute should be added.
        name (str): Name of the new attribute.
        value: Value of the new attribute.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """

    # Check if the object supports adding new attributes
    if hasattr(obj, '__dict__'):
        # Object supports adding new attributes
        setattr(obj, name, value)
    else:
        # Object does not support adding new attributes, raise TypeError
        raise TypeError("can't add new attribute")
