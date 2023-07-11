#!/usr/bin/python3
for integers in range(0, 100):
    if integers == 99:
        print("{:02d}".format(integers))
    elif integers < 99:
        print("{:02}".format(integers), end='')
