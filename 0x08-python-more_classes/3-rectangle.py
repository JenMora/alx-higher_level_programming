#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """This class represent a rectangle."""

    def __init__(self, width=0, height=0):
        """This method initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method sets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method sets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """This method return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """This method returns the printable representation of the Rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_angle = []
        for h in range(self.__height):
            [rect_angle.append('#') for w in range(self.__width)]
            if h != self.__height - 1:
                rect_angle.append("\n")
        return ("".join(rect_angle))
