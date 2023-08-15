#!/usr/bin/python3
"""
This is module for a function that readsa text file UTF8
and prints it to stdout
"""


def read_file(filename=""):
    """
    This is a method that readsa text file UTF8
    and prints it to stdout
    """

    with open(filename, "r", encoding="utf-8") as file:
        """with closes the file instead of file.close"""
        print(file.read(), end="")
