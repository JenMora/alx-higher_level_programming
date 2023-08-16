#!/usr/bin/python3
"""
this method imports sys module, save_to_json_file
and load_from_json files to add system arguments and save them to a list.
"""


from os.path import exists
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """Adds all the passed arguments to a python list"""
    filename = "add_item.json"
    new_args = sys.argv[1:]
    list_args = []

        if os.path import exists(filename)
            list_args = load_from_json_file(filename)
        else:
            list_args = []
        list_args.extend(new_args)
        save_to_json_file(list_args, filename)
