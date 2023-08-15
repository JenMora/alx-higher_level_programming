#!/usr/bin/python3
"""
This is a module that defines A function that writes an Object to a
text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    this is a method that  writes an Object to a
    text file, using a JSON representation

    args
    my obj: the object of the function
    filename: the text file to which the object will be written

    Returns
    nothing
    """

    with open(filename, "w", encoding="utf-8") as file:
        return json.dumps(my_obj)
