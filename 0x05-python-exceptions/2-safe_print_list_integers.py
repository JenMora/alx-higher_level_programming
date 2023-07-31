#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list and only integers"
    Args:
    my_list: the llist that contains the elements to be printed
    x: the integers to be printed

    Returns:
    The real number of integers printed
    """

    elements = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                elements += 1
                print("")
    except (TypeError, ValueError)
    raise


return (elements)
