#!/usr/bin/python3
"""
This is a module that writes a string to a text file (UTF8)
and returns the number of characters written
"""

def write_file(filename="", text=""):
    """
    This is a method that writes a string to a text file (UTF8)
    and returns the number of characters written
    Args
    filename="": the string to be passed
    text: the file to which the text will be added
    Returns:
    Nothing
    """

    with open(filename, "w", encoding="utf-8") as file:
        """With automatically closes the file"""
        return file.write(text)
    

