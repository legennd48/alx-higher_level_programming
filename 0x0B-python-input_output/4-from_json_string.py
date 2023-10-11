#!/usr/bin/python3
"""
Module: 4. From JSON string to Object
returns an object (Python data structure) represented by a JSON string:
"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string
    Args:
        my_str (str): json string representation
    Return:
        an object (Python data structure) represented by a JSON string
    """

    return json.loads(my_str)
