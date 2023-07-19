#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    A function that replaces all occurrences\
    of an element by another in a new list.
    Argumets:
    my_list which is the initial list
    search is the element to replace in the list
    replace is the new element
    Returns:
    A new list
    '''

    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
