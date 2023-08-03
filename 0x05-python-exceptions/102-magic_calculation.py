#!/usr/bin/python3


def magic_calculation(a, b):
    ret = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception('Too far')
                ret = ret + (a ** b) / i
    except Exception:
        ret = a + b
    return ret
