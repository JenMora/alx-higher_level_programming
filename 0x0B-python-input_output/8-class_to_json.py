#!/usr/bin/python3
"""
This is a module that returns the dictionary
description with simple data structure

(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """ this is a method that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    args
    obj:the class instance
    returns
    a dictionaru description
    """

    dict_1 = obj.__dict__
    return dict_1
