#!/usr/bin/python3
def no_c(my_string):
    """Remove both c and C
    Args:
    my_string: The string  to remove the characters c and C
    Returns:
    The new string without the characters c and C
    """
    updated_string = my_string.translate({ord(char): None for char in 'cC'})
    return (updated_string)
