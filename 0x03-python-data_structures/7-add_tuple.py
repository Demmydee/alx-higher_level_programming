#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for num in range(2):
        if len(tuple_a) >= 1:
            a = tuple_a[0]
        else:
            a = 0
        if len(tuple_b) >= 1:
            a += tuple_b[0]
        else:
            a += 0
        if len(tuple_a) >= 2:
            b = tuple_a[1]
        else:
            b = 0
        if len(tuple_b) >= 2:
            b += tuple_a[1]
        else:
            b += 0
        new_tuple = a, b
        return new_tuple
