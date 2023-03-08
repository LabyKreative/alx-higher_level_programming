#!/usr/bin/python3
for i in range(0, 100, 1):
    f = int(i / 10)
    l = int(i % 10)
    if f == l:
        continue
    if f > l:
        continue
    if i == 89:
        print("{}{}".format(f, l))
        break
    print("{}{}, ".format(f, l), end="")
