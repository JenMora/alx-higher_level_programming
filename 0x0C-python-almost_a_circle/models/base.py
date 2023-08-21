#!/usr/bin/python3
""" This is the base class module"""


import json


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
