#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    """
    Prints a matrix of integers.
    Arg:
    matrix: A list of lists containing the integers to be printed.
    Returns:
    Nothing.
    """

    for m in matrix:
        print(" ".join("{:d}".format(integer) for integer in m))
