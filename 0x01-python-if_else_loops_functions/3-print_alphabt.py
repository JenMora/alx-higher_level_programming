#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if chr(alphabet) != 'e' and chr(alphabet) != 'q':
        print(chr(alphabet).format(), end="")
