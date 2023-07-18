#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """a function that prints all integers of a list, in reverse order.
    Args:
        my_list: The list to print the integers from.
        """
    if my_list:
        for number in my_list[::-1]:
            print('{:d}'.format(number))
