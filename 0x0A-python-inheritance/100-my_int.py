#!/usr/bin/python3
"""
This is a MyInt module that prints an integer instance
"""


class MyInt(int):
    """
    This is a MyInt class that inherits from int.
    """
    def __init__(self, value):
        """
        This method initializes instance attribute value.
        """
        self.value = value

    def __eq__(self, other):
        """
        This method reverses the eq method.
        """
        return self.value != other

    def __ne__(self, other):
        """
        This method reverses the ne method.
        """
        return self.value == other
