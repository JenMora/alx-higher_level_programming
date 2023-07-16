#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        integer = 0
        new = []
        for element in my_list:
            if my_list[integer] % 2 == 0:
                new.append(True)
            else:
                new.append(False)
            integer += 1
        return new
