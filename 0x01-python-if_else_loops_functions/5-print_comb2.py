#!/usr/bin/python3
numbers = range(0, 100)
for num in numbers:
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}, ".format(num), end="")
