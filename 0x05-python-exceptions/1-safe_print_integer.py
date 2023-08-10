#!/usr/bin/python3.11.4
def safe_print_integer(value):
    """ A function that prints ann integer with "{:d}".format
    Agrs:
    Value(int)
    Returns:
    false if a type error occurs, otherwise true
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
