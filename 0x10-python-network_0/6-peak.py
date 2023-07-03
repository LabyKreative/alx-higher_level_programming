#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Defines a peak in list_of_integers"""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)
    lis = list_of_integers

    if mid - 1 < 0 and mid + 1 >= length:
        return lis[mid]
    elif mid - 1 < 0:
        return li[mid] if li[mid] > lis[mid + 1] else lis[mid + 1]
    elif mid + 1 >= length:
        return lis[mid] if lis[mid] > lis[mid - 1] else lis[mid - 1]

    if lis[mid - 1] < lis[mid] > lis[mid + 1]:
        return lis[mid]

    if lis[mid + 1] > lis[mid]:
        return find_peak(lis[mid:])
    return find_peak(lis[:mid])
