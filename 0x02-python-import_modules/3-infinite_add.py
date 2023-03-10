#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    l = sys.argv
    sum = 0
    for i in range(len(l) - 1):
        sum += int(l[i + 1])
    print("{}".format(sum))
