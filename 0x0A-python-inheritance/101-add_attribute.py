#!/usr/bin/python3
"""
This is a module that illustrates the usage of try, except
to add a new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """
    This method adds a new attribute to an object if it's possible.
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
