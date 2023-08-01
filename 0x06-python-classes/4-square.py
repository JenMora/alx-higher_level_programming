#!/usr/bin/python3
"""This is a function that defines a class Square."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """This constuctor initializes a new square.
        Arguments:
            size (int):
            The size of the new square.
        """
        self.size = size

    @property
    #"""A decorator defining the property
    #method to make size accessible
    #"""
    def size(self):
        """This method sets the current size of the square."""
        return (self.__size)

    @size.setter
    #"""This decorator allows to set
    #value to the size argument
    #"""
    def size(self, value):
        """This method contains the value size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current area of the square."""
        return (self.__size * self.__size)
