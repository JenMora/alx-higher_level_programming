#!/usr/bin/python3
"""
This is a module that returns True if the object is an instance
or if the object is an instance of a class that inherited from
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):

    """
    This a method that  returns True if the object is an instance
    or if the object is an instance of a class that inherited from
    the specified class ; otherwise False

    Args:
    obj: the object to be examined
    a_class: the specified class

    Returns:
    True if the object is an instance
    or if the object is an instance of a class that inherited from
    the specified class ; otherwise False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
