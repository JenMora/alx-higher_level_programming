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
        number_of_elements = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            number_of_elements += 1
    except IndexError:
        pass
    finally:
        print()
    return (number_of_elements)
