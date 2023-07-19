#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        num_2 = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            num_2 += (tup[1])
        return (num/num_2)
    return 0
