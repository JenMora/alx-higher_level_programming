#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
        return None
    finally:
        print("Inside result: {}".format(div))
        return division
