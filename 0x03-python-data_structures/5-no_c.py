#!/usr/bin/python3

def no_c(my_string):
    string_new = ""
    for st in range(len(my_string)):
        if my_string[st] == "c" or my_string[st] == "C":
            string_new += ""
        else:
            string_new += my_string[st]
    return string_new
