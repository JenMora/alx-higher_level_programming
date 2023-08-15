#!/usr/bin/python3
"""
This is a module that defines A function that creates an Object from
JSON representation
"""

import json


def load_from_json_file(filename):
    """
    this is a method that  creates an Object from a JSON representation

    args
    my obj: the object of the function
    filename: the text file to which the object will be written

    Returns
    the created file
    """

    with open(filename, 'r') as file:
        a_file = json.load(file)
        return a_file
