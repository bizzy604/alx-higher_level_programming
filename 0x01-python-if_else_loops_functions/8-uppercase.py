#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            upp_char = chr(ord(i) - 32)
        else:
            upp_char = i
        print("{:s}".format(upp_char), end="")
    print()
