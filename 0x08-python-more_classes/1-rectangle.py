#!/usr/bin/python3
"""
This is a class that defines a rectangle based on 0-rectangle.py
"""


class Rectangle:
    """
    This class represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        This method initializes the rectangle
        args:
        width: The int width of the new rectangle
        height: the height int of the new recctangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """
            This method fetches the rectangle width
            """
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

            """ This method gets the rectangle height"""
            return self.__height

        @height.setter
        def height(self, value):

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
