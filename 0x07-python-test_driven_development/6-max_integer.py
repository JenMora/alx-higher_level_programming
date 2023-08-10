#!/usr/bin/python3
"""
This is a module that contains max_integer function with Unittests

"""


def max_integer(list=[]):
    """
    This method finds and returns the max integer in a list of integers
    The function returns None if the list is empty
    Arguments:
        list: The listwith integers
    Return: max integer in a list of integers, Noe if the kist is empty
    """
    if len(list) == 0:
        return None
    ret = list[0]
    if type(ret) is not int and type(ret) is not float:
        raise TypeError("result must be an integer")
    integer = 1
    while integer < len(list):
        if list[integer] > ret:
            ret = list[integer]
        integer += 1
    return ret
