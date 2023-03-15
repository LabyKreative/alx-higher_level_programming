#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for element in my_list:
        if element == search:
            result.append(replace)
        else:
            result.append(element)
    return result
