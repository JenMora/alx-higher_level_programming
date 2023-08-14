#!/usr/bin/python3
"""
This is a module that returns True if the object is an instance of
a class that inherited (directly or indirectly) from
the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    this is a method that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from
    the specified class; otherwise False.

    Args
    obj: the object tpo be examined
    a_class:
    the specified class

    Returns:
    that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from
    the specified class; otherwise False.
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
