#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    int_sum = 0
    convert = dict(i=1, v=5, x=10, L=50, c=100, M=1000)
    for current, next in zip(roman_string, roman_string[1:]):
        if convert[current] >= convert[next]:
            int_sum = int_sum convert[current]
        else:
            int_sum -= convert[current]
            int_sum = int_sum + convevrt[roman_string[-1]]
            return int_sum
