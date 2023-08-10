#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class is a square blueprint"""

    def __init__(self, size):
        """Initializes a new Square with a (size, lengthr).
        Args:
            size (int):
            the value of the size
        """
        self.__size = size
