#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 0-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:

    """
    This class defines a square
    Args:
    __size(int): The size of the square(one side)
    """

    def __init__(self, size):

        """
        initializes a new square with the given size
        Args:
        the size(int)
        """
    self.__size = size
