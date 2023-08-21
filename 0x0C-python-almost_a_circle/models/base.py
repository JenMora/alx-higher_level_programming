#!/usr/bin/python3
""" This is the base class module"""


class Base:
    """The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The initializer"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
