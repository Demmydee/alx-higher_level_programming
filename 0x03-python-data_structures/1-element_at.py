#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        exit(None)
    idx = my_list[idx]
    return(idx)
    """print("Element at index {} is {}".format(idx, my_list[idx - 1]))"""
