#!/usr/bin/python3
if __name__ == "__main__":
    """A function that prints the number of arguments parsed\
            to the command lines"""
    import sys
    count = len(sys.argv)
    if count == 1:
        print("0 argumnets.")
    else:
        if count == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(count - 1))
    for arg in range(1, count):
        print("{}: {}".format(arg, sys.argv[arg]))
