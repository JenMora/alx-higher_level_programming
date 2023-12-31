#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """This private constructor initialize a new Square.
        Arguments:
            size (int):
            The size of the new square to be formed
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
