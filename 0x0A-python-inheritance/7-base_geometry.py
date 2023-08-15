#!/usr/bin/python3
"""
This is a module that defines a BaseGeometry class
Based on 6-Base_geometry.py
"""


class BaseGeometry:
    """
    This is a class that defines BaseGeometry
    """

    def area(self):
        """ This is a method that implements area in BaseGeometry Class
        args:
        none
        Returns:
        none
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is a method that validates the value argument
        Args:
        name: the string argument
        value: the integer value
        Returns
        Nothing
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

        if __name__ == "__main__":
            import doctest
            doctest.testfile("rest/7-base_geometry.txt")
