#!/usr/bin/python3
"""This is a module with a function that defines a class Square."""


class Square:
    """This class defines a square."""

    def __init__(self, size):
        """Initialize a new square.
        Arguments:
            size (int):
            The size of the new square.
        """
        self.size = size

    @property
    # A decorator defining the property
    # method to make the size argument accessible
    def size(self):
        """This method sets the current size of the square."""
        return (self.__size)

    @size.setter
    # This decorator allows to set
    # value to the size argument
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ This method return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """This method print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for a in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
