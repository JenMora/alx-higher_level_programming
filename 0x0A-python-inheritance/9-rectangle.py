#!/usr/bin/python3
"""A module that defines a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A method that writes a rectangle that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py)

    Args
    width: of the rectangle
    height: of teh rectangle

    Returns: Nothing
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This method returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """This is the string representation method"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
