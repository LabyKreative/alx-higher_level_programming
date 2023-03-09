#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print("Number of argument(s): {}.".format(num_args))
        print("Argument{}:".format("" if num_args == 1 else "s"))
        for i in range(num_args):
            print("{}: {}".format(i+1, sys.argv[i+1]))
