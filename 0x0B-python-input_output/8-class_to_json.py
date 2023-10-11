#!/usr/bin/python3
"""
Module: 8. Class to JSON
returns the dictionary description with simple
data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object:
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure"""
    return (obj.__dict__)
