#!/usr/bin/python3
"""This function defines a class Square."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """This private constructor initialize a new Square.
        Arguments:
            size (int):
            The size of the new square to be formed
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
