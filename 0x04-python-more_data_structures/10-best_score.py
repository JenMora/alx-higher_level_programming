#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    returns = list(a_dictionary.keys())[0]
    maximum = a_dictionary[returns]
    for key, argument in a_dictionary.items():
        if argument > maximum:
            big = argument
            returns = key
    return (returns)
