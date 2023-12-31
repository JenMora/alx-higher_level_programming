#!/usr/bin/python3
"""
Module contains Square class
inherited from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle class and
    instantiatiates of private instance attribute: size.
    """
    def __init__(self, size):
        """
        This method initialiazes private instance attribute: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This method calculates and returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the square
        """
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)

    def __str__(self):
        """
        Returns the  string representation of an the square
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
