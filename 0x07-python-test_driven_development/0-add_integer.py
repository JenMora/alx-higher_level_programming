#!/usr/bin/python3
"""
This module has the add_integer function
add_integer function: This function calculates sum of two integers a and b
and prints the result to stdout
TypeError occurs when a or b is not an integer
"""


def add_integer(a, b=98):
    """
    This method calculates the sum of two integers: a and b
    Arguments:
        a: the first integer
        b: the second integer
    Returns: a + b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
