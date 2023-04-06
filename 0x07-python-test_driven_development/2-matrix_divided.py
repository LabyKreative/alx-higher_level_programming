#!/usr/bin/python3
"""Defines a matrix division"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): a list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: if the matrix contains non-numbers.
        TypeError: if the matrix contains rows of different sizes.
        TypeError: if div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elm, int) or isinstance(elm, float))
                    for elm in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
