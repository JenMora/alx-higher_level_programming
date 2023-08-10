#!/usr/bin/python3
"""This module has the magic_calculation function"""

def magic_calculation(a, b):
    aresult = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception('Too far')
            aresult += (a ** b) / i
    except Exception:
        aresult = a + b
    return aresult
