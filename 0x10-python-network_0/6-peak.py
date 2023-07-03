#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def FindAPeak(arr, x, y):
    """Binary Search"""
    mid = int((x + y) / 2)
    # if mid element is peak
    if (mid == len(arr)-1 or arr[mid] >= arr[mid+1]) and\
       (mid == 0 or arr[mid] >= arr[mid-1]):
        return arr[mid]
    # when your peak exists in the right half
    if arr[mid] < arr[mid+1] and mid+1 < len(arr):
        return FindAPeak(arr, mid+1, y)
    # when your peak exists in the left half
    else:
        return FindAPeak(arr, x, mid-1)

def find_peak(list_of_integers):
    """Defines a peak in list_of_integers"""
    my_lisy = list_of_integers

    if len(my_list) == 0:
        return None

    peak = FindAPeak(my_list, 0, len(my_list) - 1)
    return peak
