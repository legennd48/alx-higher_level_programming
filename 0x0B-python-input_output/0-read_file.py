#!/usr/bin/python3
"""
Module: 0-read_file
reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, mode="r", encoding="utf-8") as x:
        print(x.read(), end="")
