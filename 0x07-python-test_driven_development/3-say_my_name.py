#!/usr/bin/python3
"""
This module contains say_my_name function
The function checks if name is a string
and prints first_name and last_name to stdout
A TypeError is raised when first_name or lastname is not a string
"""


def say_my_name(first_name, last_name=""):
    """
    This method prints the first and last name to stdout.
    Arguments:
        str: first_name
        str:last_name
    Returns: first_name, last_name if both names are strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
