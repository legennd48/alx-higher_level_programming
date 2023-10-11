#!/usr/bin/python3
"""
Module: 13. Search and update
Inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a string after lines that include a specific keyword in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The keyword to search for in each line.
        new_string (str): string to append after lines containing the keyword.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """

    try:
        with open(filename, mode="r+", encoding="utf-8") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                f.write(line)
                if search_string in line:
                    f.write(new_string)
            f.truncate()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
