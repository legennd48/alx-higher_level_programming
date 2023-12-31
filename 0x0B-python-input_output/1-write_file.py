#!/usr/bin/python3
'''
Module: 1. Write to a file
'''


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): Path of file to be written to.
        text (str): Test to be written.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
