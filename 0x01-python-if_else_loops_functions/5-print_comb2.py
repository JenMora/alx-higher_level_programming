#!/usr/bin/python3
for integers in range(0, 100):
    if integers == 99:
        print("{}".format(integers))
    else:
        print("{:02}".format(integers), end=",")
