#!/usr/bin/python3
"""
This is a module for a function that returns the
python data structure of an object from a json string
"""
import json


def from_json_string(my_obj):
    """ This is a method that returns the
    python data structure of an object from a json string
    Args
    my_obj
    Returns
    JSON representation of my_obj
    """
    from_json_string = json.loads(my_obj)
    return from_json_string
