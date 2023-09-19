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

        args_num = len(args)
        if args_num >= 1:
            self.id = args[0]
        if args_num >= 2:
            self.size = args[1]
        if args_num >= 3:
            self.x = args[2]
        if args_num >= 4:
            self.y = args[3]

    def update(self, *args, **kwargs):
        """
        Replace args with kwargs, changing attributes

        """
        if args:
            attr = ["id", "size", "x", "y"]
            for items in range(len(args)):
                setattr(self, attr[items], args[items])
        elif kwargs:
            for key, value in kwargs.items():
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
