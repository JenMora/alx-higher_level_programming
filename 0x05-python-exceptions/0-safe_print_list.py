#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    """A function that prints x elements of a list
    Args:
    my_list
    x integer
    Returns:
    The real number of elements printed
    """

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            print("")
            return x
    except (IndexError, TypeError):
        print("")
    return (i)
