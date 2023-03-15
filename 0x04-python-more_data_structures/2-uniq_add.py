#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    for n in dict.fromkeys(my_list):
        s += n
    return s
