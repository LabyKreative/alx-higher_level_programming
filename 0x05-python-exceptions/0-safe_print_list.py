#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in my_list[:x]:
            print("{}".format(i), end='')
            num += 1
        print('')
        return num
    except:
        print("Error occurred")
