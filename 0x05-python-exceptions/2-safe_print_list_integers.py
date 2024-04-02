#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0
    try:
        while (count < x):
            if isinstance(my_list[count], int):
                print("{:d}".format(my_list[count]), end="")
                printed += 1
            count += 1
    except IndexError:
        raise
    else:
        print("")
        return (printed)
