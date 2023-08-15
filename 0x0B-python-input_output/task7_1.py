#!/usr/bin/python3
"""
This is a module that defines functions taht add all arguments to a python list
and then saves the arguments to a file
The list must be saved as a JSON representation
"""

from os.path import exists
import sys
from typing import List
# imporit from 5-save_to_json_file.py
# import from 6-load_from_json_file.py


def save_to_json_file(my_obj, filename):
    """
    this is a method that  writes an Object to a
    text file, using a JSON representation

    args
    my obj: the object of the function
    filename: the text file to which the object will be written

    Returns
    the written file
    """

    with open(filename, "w", encoding="utf-8") as file:
        a_file = json.dumps(my_obj)
        return file.write(a_file)


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


if __name__ == "__main__":
    """Adds all the passed arguments to a python list"""
    filename = "add_item.json"
    new_args = sys.argv[1:]
    list_args = []

    try:
        if exists(filename):
            list_args = load_from_json_file(filename)
        else:
            list_args = []
        list_args.extend(new_args)
    finally:
        save_to_json_file(list_args, filename)
