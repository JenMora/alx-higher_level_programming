#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    A function that finds the biggest integer of a list.
    Agrs:
    my_list: the list to check
    Returns:
    The biggest integer of the list, or None if the list is empty.
    """

    if not my_list: 
        return None
    else:
        max_integer = my_list[0]
    for integer in range (len(my_list)):
        if my_list[integer]> max_integer:
            max_integer = my_list[integer]
            return (max_integer)
