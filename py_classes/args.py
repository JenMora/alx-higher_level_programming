#!/usr/bin/python3
def test_arg_kwargs(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

args = (2, 3, 5)
test_arg_kwargs(*args)
arg1: 2
arg2: 3
arg3: 5
