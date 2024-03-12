#!/usr/bin/python3
for i in range(10):
    for b in range(i + 1, 10):
        if i == 8 and b == 9:
            print("{:d}{:d}".format(i, b))
        else:
            print("{:d}{:d}".format(i, b), end=", ")
