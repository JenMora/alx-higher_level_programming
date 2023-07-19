#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''a function that adds all unique integers\
        in a list (only once for each integer
        Arguments:
        my_list
        Return:
        A new list
        '''

    return sum(set(my_list))
