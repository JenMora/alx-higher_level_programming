#!/usr/bin/python3
def magic_calculation(a, b):

    '''Write the Python function def magic_calculation(a, b):\
            that does exactly the same as the Python bytcode provided'''
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for integer in range(4, 6):
            c = add(c, integer)
            return (c)
        else:
            return (sub(a, b))
