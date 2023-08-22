#!/usr/bin/python3
"""This is a rectangle module"""


from models.base import Base


class Rectangle(Base):
    """This is a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This method instantiates the class Base"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ represents the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ defines the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets vakue for the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """represents the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value to the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ this is the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of the y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """defines the rectangle area"""
        return self.width * self.height

    def display(self):
        """displays the rectangle"""
        for items in range(self.y):
            print()
        for items in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ returns a string representation"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.height)

    def update(self, *args):
        """updates the rectangle arguments, changing attributes"""
        arg_num = len(args)
        if arg_num >= 1:
            self.id = args[0]
        if arg_num >= 2:
            self.width = args[1]
        if arg_num >= 3:
            self.height = args[2]
        if arg_num >= 4:
            self.x = args[3]
        if arg_num >= 5:
            self.y = args[4]

    def update(self, *args, **kwargs):
        """Replace args with kwargs, changing attributes"""
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for items in range(len(args)):
                setattr(self, attr[items], args[items])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
