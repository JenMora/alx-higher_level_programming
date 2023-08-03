#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    """A function that prints x elements of a list
    Args:
    my_list- which contains any type of data
    x the  number of elements to print
    Returns:
    The real number of elements printed
    """

    elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements = elements + 1
        except IndexError:
            break
        print("")
        return (elements)
