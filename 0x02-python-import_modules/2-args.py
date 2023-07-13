#!/usr/bin/python3
if __name__ == "__main__":
    """A function that prints the number of arguments parsed\
            to the command lines"""
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 argumnets:")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
        for arg in range(count):
            print("{}:{}".format(arg + 1, sys.argv[arg + 1]))
