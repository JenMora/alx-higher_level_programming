#!/usr/bin/python3
"""This module has ths Safe_print_integer function"""
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(str(e)))
        sys.stderr.flush()
        return False
