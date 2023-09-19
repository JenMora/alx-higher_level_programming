#!/usr/bin/python3
"""
This is the base class module

"""


import json
import csv
import turtle


class Base:
    """The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The initializer"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a JSON representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A mrthod that writes the JSON string representation of
        list_objs to a file
        """

        if list_objs is None:
            list_obj = []

        a_file = cls.__name__ + ".json"
        with open(a_file, "w") as file:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(list_dicts)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 6)  # this is a rectangle dummy instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(6)  # this is a square dummy instance
        else:
            dummy_instance = None
        if dummy_instance:
            dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        a_file = cls.__name__ + ".json"
        try:
            with open(a_file, "r") as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                instances = [cls.create(**dict) for dict in list_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        if list_objs is None or list_objs == []:
            return
        class_name = cls.__name__
        a_file = class_name + ".csv"
        with open(a_file, "w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if class_name == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif class_name == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(row)
        json_output = json.dumps([(obj.to_dictionary())
                                 for obj in list_objs])
        print(json_output)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes CSV"""
        a_file = cls.__name__ + ".csv"
        objects = []
        try:
            with open(a_file, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, height, width, x, y = map(int, row)
                        instance = cls(width, height, x, y, id)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        instance = cls(size, x, y, id)
                        objects.append(instance)
        except FileNotFoundError:
          pass
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        from models.rectangle import Rectangle
        from models.square import Square
        from models.base import Base

        window = turtle.Screen()
        window.bgcolor("Green")

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for items in range(4):
                turtle.forward(rect.width)
                turtle.left(45)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for items in range(8):
                turtle.forward(square.size)
                turtle.left(45)

        turtle.done()
