#!/usr/bin/python3
def print_last_digit(number):
    d = -number % 10 if number < 0 else number % 10
    print("{}".format(d), end="")
    return d
