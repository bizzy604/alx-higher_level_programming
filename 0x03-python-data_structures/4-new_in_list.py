#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        copy = []
        for a in my_list:
            copy.append(a)
        return copy
    else:
        copy = []
        for a in my_list:
            copy.append(a)
        copy[idx] = element
        return copy
