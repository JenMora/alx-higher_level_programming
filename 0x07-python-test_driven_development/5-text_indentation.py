#!/usr/bin/python3
"""
This module prints a text with 2 new lines after ., ? and :
This module contains the function text_indentation    
"""


def text_indentation(text):
    """
    The text Indentation Method prints a text with 2 new lines after ., ? and :
    Args:
    text: the argument parsed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text_length = len(text)
    s = 0
    while (s < text_length):
        if text[s] in (".", "?", ":"):
            if (s + 1) != text_length:
                string = text[s + 1]
                if (string != '.' and string != '?' and string != ':'):
                    print(text[s], end='\n\n')
                    if string == ' ':
                        s += 2
                    if string != ' ':
                        s += 1
        else:
            print(text[s], end='')
            s += 1
