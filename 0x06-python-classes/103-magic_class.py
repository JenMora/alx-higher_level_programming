import math
""" 
A Python class MagicClass that does exactly the
same as the given Python bytecode
"""
class MagicClass:
    """
    A class representing a circle with magic calculations for area and circumference.

    Attributes:
        __radius (float):
        The circle radius.
    """

    def __init__(self, radius):
        """
        This method initialize the MagicClass with the given radius.

        Args:
            radius (float):
            The radius of the circle. It must be a number (integer or float).

        Raises:
            TypeError:
            If the provided radius is not a number (integer or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        This method calculates the area of the circle.

        Returns:
            float:
            The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        This method calculate the circumference of the circle.

        Returns:
            float:
            The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

