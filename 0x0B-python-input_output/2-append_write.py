#!/usr/bin/python3
""" This is a module that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    This is a method that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    args
    text: the file to which we are appending
    filename: the string to append
    """

    with open(filename, "a", encoding="utf-8") as file:
        # a is used to append a file to an existing file and with is used
        # to close the fie after appending
        return file.write(text)
