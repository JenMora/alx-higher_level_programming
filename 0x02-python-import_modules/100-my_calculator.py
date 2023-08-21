#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul,div
if __name__ == "__main__":
    arg = len(sys.argv)
    if arg != 4:
    a = int(sys.argv((1)))
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {result}")
