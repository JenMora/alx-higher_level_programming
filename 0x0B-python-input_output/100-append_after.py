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

    content = []

    with open(filename, 'r', encoding='utf-8') as i_file:
        # this line of code reads the contens of the file
        content = i_file.readlines()
        count = 0
        while count < len(content):
            # iterate over each line with a while loop and a counter count
            if search_string in content[count]:
                # check of a search_string in each line
                content[count:count + 1] = [content[count], new_string]
                count += 1
            count += 1

    with open(filename, "w", encoding='utf-8') as i_file:
        i_file.writelines(content)
