#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    """A function that prints x elements of a list
    Args
    my_list

    Returns
    The real number of elements printed
    """

    number_of_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            number_of_elements += 1
    except IndexError:
        pass
        print("cannot output x because it is out of range")
    return number_of_elements
