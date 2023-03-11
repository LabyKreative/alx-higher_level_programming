#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for char in my_string:
        if char != "c" and char != "C":
            new_string.append(char)
    return "".join(new_string)
