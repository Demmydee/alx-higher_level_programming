#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keylist = list(a_dictionary.keys())
    for val_value in keylist:
        if value == a_dictionary.get(val_value):
            del a_dictionary[val_value]
    return (a_dictionary)
