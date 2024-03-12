#!/usr/bin/python
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            upper_char = chr(ord(i) - 32)
        else:
            upper_char = i
            print("{:s}".format(upper_char), end="")
            print()
