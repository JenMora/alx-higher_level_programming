#!/usr/bin/python3
"""

This is module that divides an element by a number indicated

"""


def matrix_divided(matrix, div):
    """
    This method divides the elements of a matrix
    """
    if isinstance(div, int) == 0 and isinstance(div, float) == 0:
        raise TypeError("div must be a number")
    a_matrix = []
    num = 0
    for row in matrix:
        t = []
        for element in row:
            if isinstance(element, int) or isinstance(element, float):
                t.append(round((element / div), 2))
            else:
                a_row = "matrix must be a matrix (list of lists)"
                a_size = " of integers/floats"
                raise TypeError(s + n)
        if num != 0:
            if num != len(row):
                a_row = "Each row of the matrix"
                a_size = " must have the same size"
                raise TypeError(a_row + a_size)
        num = len(row)
        a_matrix.append(t)
    return a_matrix
