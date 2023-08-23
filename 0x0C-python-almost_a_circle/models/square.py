#!/usr/bin/python3
"""
This is a module that defines a square

"""


from models.rectangle import Rectangle
"""
This is the parent class to the square child class

"""


class Square(Rectangle):
    """
    This is a class square inheriting from rectangle and the
    grandchild to Base

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the side size of the square

        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Get the size value of the square width

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates attributes of the square

        """
        if args:
            attr = ["size", "id", "x", "y"]
            for items in range(len(args)):
                setattr(self, attr[items], args[items])
            # if len(args) >= 2:
                # self.size = args[1]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        represents a square dictionary

        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """
        This is a method that returns the print()
        and str() representation of a Square.

        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
