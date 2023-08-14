#!/usr/bin/python3
""" This is a module  for returning a list of available attributes
and methods of an object
Arguments:
    none
    Returns:
    A list object
"""


def lookup(obj):
    """
    This method returns a list of ojects using teh inbuilt ("dir")command
    args:
    obj
    returns
    a list of objects
    """

    return dir(obj)
