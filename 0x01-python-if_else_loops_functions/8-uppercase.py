#!/usr/bin/python
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upper_char = chr(ord(i) - 32)
            print(upper_char, end='')
        else:
            print(i, end='')
    print()
