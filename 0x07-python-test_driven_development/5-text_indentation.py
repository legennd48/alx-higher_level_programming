#!/usr/bin/python3
"""
MODULE: text_indentation module
Function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""

def text_indentation(text):

    """
    Print text with 2 new lines after using '.? and :'
    Args:
    text (str): The input string.
    Raises:
    TypeError: If the input is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end='')
        if text[index] == '\n' or text[index] in ".?:":
            if text[index] in ".?:":
                print('\n')
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
