#!/usr/bin/python3
"""The module  defines a Rectangle class."""


class Rectangle:
    """This class  represents a rectangle.
    Attributes:
    number_of_instances (int): The number of Rectangle instances
    print_symbol (any): The symbol used for string reprensative
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1

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
        """Thismethod sets the height of the Rectangle."""
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

    @staticmethod
    def bigger_or_equal(rect_angle_1, rect_angle_2):
        """
        This method returns the bigger rectangle
        Args:
        rect_angle_1: The first rectangle.
        rect_angel_2: The second rectangle

        Raises:
        TypeError: If either of first or the second argument is a rectangle
        """

        if not isinstance(rect_angle_1, Rectangle):
            raise TypeError("rect_angle_1 must be an instance of Rectangle")
        if not isinstance(rect_angle_2, Rectangle):
            raise TypeError("rect_angle_2 must be an instance of Rectangle")
        if rect_angle_1.area() >= rect_angle_2.area():
            return (rect_angle_1)
        return (rect_angle_2)

    @classmethod
    def square(cls, size=0):
        """
        This method returns a new rectangle with width
        and height equaling to size
        Args:
        size: The width and henight of teh new Rectangle
        """
        return (cls(size, size))

    def __str__(self):
        """This method returns the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_angle = []
        for h in range(self.__height):
            [rect_angle.append(str(self.print_symbol))
             for w in range(self.__width)]
            if h != self.__height - 1:
                rect_angle.append("\n")
        return ("".join(rect_angle))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect_angle = "Rectangle(" + str(self.__width)
        rect_angle += ", " + str(self.__height) + ")"
        return (rect_angle)

    def __del__(self):
        """ This method prints a message for
        every deletion of the rectangle.
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
