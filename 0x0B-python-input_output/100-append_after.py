#!/usr/bin/python3
"""
This is a module that defines a function that
inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This is a method that defines a function that
    inserts a line of text to a file, after each line
    containing a specific string
    """

    try:
        with open(filename, 'r') as file:
            content = file.readlines()

        found = False
        for i, line in enumerate(content):
            if search_string in line:
                content.insert(i + 1, new_string)
                found = True
                break

        if not found:
            content.append(new_string)

        with open(filename, 'w') as file:
            file.writelines(content)

    except FileNotFoundError:
        with open(filename, 'w') as file:
            file.write(new_string)
