#!/usr/bin/python3
"""
    This module adds all arguments to a Python list
    and saves them in a file
"""


import sys
from os import path
from typing import List


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item_json_file(file: str, new_args: List[str]):
    """
        This method creates a list, the args in the lists are added
        saved the updated list to a file

        file: the files from the imported modules
        args: the diffrent arguments args to be added/appended
    """
    if not path.exists(file):
        save_to_json_file([], file)

    list_update = load_from_json_file(file)
    list_update.extend(args)

    save_to_json_file(list_updatet, file)


if __name__ == '__main__':
    file = 'add_item.json'
    new_args = sys.argv[1:]
    funct_adds_to_list(file, new_args)
