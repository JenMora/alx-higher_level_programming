#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division_result = a / b
    except ZeroDivisionError:
        division_result = None
        return None
    finally:
        print("Inside result: {}".format(divsion_result))
        return division_result
