#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    l = sys.argv
    sum = 0
    for i in range(1, len(l)):
        sum += int(l[i])
    print("{}".format(sum))
