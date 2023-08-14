#!/usr/bin/python3
"""
This module writes a class Square that inherits
from Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    this class represents a square"""


    def __init__(self, size):
        """
        This method initializes a Square instance.
        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
    def area(self):
        """
        This method calculates the area of the square.
        Returns:
            the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
