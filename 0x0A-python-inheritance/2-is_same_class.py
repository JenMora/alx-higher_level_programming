#!/usr/bin/python3
""" This is a module that defines a class that returns true if
the object is exactly as the instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    This is a method that that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    Arguments:
    obj:the object to be examined
    a_class: the specified class
    Returns
    True if the object is exactly an instance in a specified class
    on sucess, otherwise False
    """ 

    if type(obj) == a_class:
        return True
    else:
        return False
