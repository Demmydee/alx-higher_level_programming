#!/usr/bin/python3
arr = range(97, 123)
for alpha in arr:
    if (alpha != 113 and alpha != 101):
        print("{}".format(chr(alpha)), end="")
