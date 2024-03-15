#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        exit(None)
    my_list[idx] = element
    return(my_list)
    """print("Element at index {} is {}".format(idx, my_list[idx - 1]))"""
