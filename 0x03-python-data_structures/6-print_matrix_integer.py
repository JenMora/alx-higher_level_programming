#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Args:
    matrix: A list of lists containing the integers to be printed.
    Returns:
    Nothing.
    """

    for row in matrix:
        print(" ".join([str(coloumn) for coloumn in row]))
