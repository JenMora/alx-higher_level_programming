#!/usr/bin/python3
"""
A module tha defines a class class Student
"""


class Student:
    """
    This class defines a student by first_name
    last_name and age
    """

    def __init__(self, first_name, last_name, age):
        """
        This method defines a student by first_name
        last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This public method retrieves a dictionary representation
        of a student in class Student
        """
        if isinstance(attrs, list):
            stdout = {}
            for obj in attrs:
                if isinstance(obj, str) and hasattr(self, obj):
                    stdout[obj] = getattr(self, obj)
            return stdout
        else:
            return self.__dict__
