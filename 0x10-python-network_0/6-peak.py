#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Defines a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
        left = 0
        right = len(list_of_integers)
        middle = ((right - left) // 2) + left
        middle = int(middle)
        if right == 1:
            return list_of_integers[0]
        if right == 2:
            return max(list_of_integers)
        if list_of_integers[mid] >= list_of_integers[mid - 1] and\
                list_of_integers[middle] >= list_of_integers[mid + 1]:
            return list_of_integers[middle]
        if middle > 0 and list_of_integers[middle] < list_of_integers[middle + 1]:
            return find_peak(list_of_integers[middle:])
        if middle > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
            return find_peak(list_of_integers[:middle])
