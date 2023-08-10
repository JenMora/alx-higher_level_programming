#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list and only integers"
    Arguments:
    my_list: the list that contains the elements to be printed
    x: the integers to be printed

    Returns:
    The real number of integers printed
    """

    element = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                element += 1
        print("")
    except IndexError:
        raise
    return element
