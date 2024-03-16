#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    y = 0
    for num in my_list:
        y -= 1
        print("{}".format(my_list[y]))
