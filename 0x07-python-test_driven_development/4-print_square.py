#!/usr/bin/python3
"""
This is a module prints a square with the character #
"""


def print_square(size):
    """
    This method prints a square with the character #
    Args:
    size: the length of the poison
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif (type(size) is float) and size < 0:
        raise TypeError("size must be an integer")

    for s in range(size):
        for s_2 in range(size):
            print("#", end='')
        print()
