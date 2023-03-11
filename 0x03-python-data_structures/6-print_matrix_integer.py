#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    if not matrix[0]:
        print()
    for j in range(x):
        y = len(matrix[j])
        for i in range(y):
            if i == y - 1:
                print("{:d}".format(matrix[j][i]))
            else:
                print("{:d} ".format(matrix[j][i]), end="")
        print()
