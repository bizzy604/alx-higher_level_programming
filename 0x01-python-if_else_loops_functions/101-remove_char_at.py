#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        var = str[0: n] + str[n + 1:]
    else:
        return str
