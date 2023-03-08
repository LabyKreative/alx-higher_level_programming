#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str):
        return str
    s = ""
    for i in range(len(str)):
        if i == n:
            continue
        s = s + str[i]
    return(s)
