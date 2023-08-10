#!/usr/bin/python3
"""This module has the safe division function"""
def safe_print_division(a, b):
    try:
        division_result = a / b
    except ZeroDivisionError:
        division_result = None
        return None
    finally:
        print("Inside result: {}".format(division_result))
        return division_result
