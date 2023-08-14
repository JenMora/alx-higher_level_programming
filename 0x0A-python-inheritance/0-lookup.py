#!/usr/bin/python3
""" This is a module  for returning a list of available attributes
and methods of an object
Arguments:
    none
    Returns:
    A list object
"""


def lookup(obj):
    return dir(obj)
