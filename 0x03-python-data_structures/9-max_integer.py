#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    A function that finds the biggest integer of a list.
    Agrs:
    my_list: the list to check
    Returns:
    The biggest integer of the list, or None if the list is empty.
    """

    if len(my_list) == 0:
        return ("None")
    integer = my_list[0]
    for i in my_list:
        if i > integer:
            integer = i
    return (integer)
