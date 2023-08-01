#!/usr/bin/python3
"""This function defines a class Square."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """This constuctor initializes a new square.
        Arguments:
            size (int):
            The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method returns the current area of the square."""
        return (self.__size * self.__size)
