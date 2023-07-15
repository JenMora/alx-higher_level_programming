#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples and returns a tuple with the sum of the first two elements
    Args:
    tuple_a: The first tuple.
    tuple_b: The second tuple.
    Returns:
    A tuple with the sum of the first two elements of each argument.
    """


    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
