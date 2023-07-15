#!/usr/bin/python3
def no_c(my_string):
    """Remove both c and C
    Args:
    my_string: The string  to remove the characters c and C
    Returns:
    The new string without the characters c and C
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string = new_string + char
            return (new_string)
