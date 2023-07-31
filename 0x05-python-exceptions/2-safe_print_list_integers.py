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
    for i in range(0, x):
        try:
            print("{:d}".format(my_list), end="")
            elements += 1
        except (TypeError, ValueError)
        continue
    print("")
    return (elements)
