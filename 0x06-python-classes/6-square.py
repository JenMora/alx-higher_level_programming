#!/usr/bin/python3
"""This is a function that defines a class Square."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Arguments:
            size (int): The size of the new square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    # This decorator makes the size argument accessible
    def size(self):
        """This method retrieves the current size of the square."""
        return self.__size

    @size.setter
    # This decorator enable the assignment of the size argument value
    def size(self, value):
        """This method sets the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    # this decorator defines the position method property
    def position(self):
        """This method retrieves the current position of the square."""
        return self.__position

    @position.setter
    # this decorator defines the position of the new square
    def position(self, value):
        """This method sets the current position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value) or \
           not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """This method prints the square with the '#' character."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
