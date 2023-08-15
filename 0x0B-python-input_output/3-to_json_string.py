#!/usr/bin/python3
"""
This is a module for a function that returns the
JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """ This is a method that  returns the
    JSON representation of an object (string)
    Args
    my_obj
    Returns
    JSON representation of my_obj
    """
    to_json_string = json.dumps(my_obj)
    return to_json_string
