#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def for_add():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} + {} = {}".format(a, b, add(a, b)))


def for_min():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} - {} = {}".format(a, b, sub(a, b)))


def for_mul():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} * {} = {}".format(a, b, mul(a, b)))


def for_div():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} / {} = {}".format(a, b, div(a, b)))


def main():
    if (len(sys.argv) - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif sys.argv[2] == "+":
        for_add()
    elif sys.argv[2] == "-":
        for_min()
    elif sys.argv[2] == "*":
        for_mul()
    elif sys.argv[2] == "/":
        for_div()
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
