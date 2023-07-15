#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for coloumn in row:
            if coloumn == row[-1]:
                print('{:d}'.format(coloumn), end=" ")
    else:
        print('{:d}'.format(coloumn), end="")
        print()
