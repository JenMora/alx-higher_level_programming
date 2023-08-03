#!/usr/bin/python3

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
