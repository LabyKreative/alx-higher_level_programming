def safe_print_list_integers(my_list=[], x=0):
    num_integers_printed = 0
    for elem in my_list[:x]:
        try:
            integer = int(elem)
            print("{:d}".format(integer), end="")
            num_integers_printed += 1
        except (ValueError, TypeError):
            pass
    print("")
    return num_integers_printed
