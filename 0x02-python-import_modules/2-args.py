#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 1
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(a, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in sys.argv[1:]:
            print("{}: {}".format(a, i))
            a += 1
