#!/usr/bin/python3
def safe_print_division(a, b):
    """ a function that divides 2 integers and prints the result.
    args:
    a and b which are integers
    returns:
     the value of the division, otherwise: None
     """

     try:
         division = a / b
     except (TypeError, ZeroDivisionError):
         division = None
     finally:
         print("The correct output must be printed and formatted correctly")
     return division
