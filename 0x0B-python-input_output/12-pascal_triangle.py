#!/usr/bin/python3
"""
This is a module that returns a list of lists of integers
"""


def pascal_triangle(n):
    """
    This method generate Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
