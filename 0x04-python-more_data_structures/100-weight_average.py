#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sco = 0
    wgh = 0

    for num in my_list:
        sco += num[0] * num[1]
        wgh += num[1]

    return (sco / wgh)
