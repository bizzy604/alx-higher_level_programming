#!/usr/bin/python
def print_last_digit(number):
    if number < 0:
        num = abs(number) % 10
        print(num, end="")
        return num
    else:
        last_digit = number % 10
        print(last_digit, end="")
        return last_digit
