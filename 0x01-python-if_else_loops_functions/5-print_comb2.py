#!/usr/bin/python3
number = range(0, 100)
for num in number:
    if num == 99:
        print(f"{num}")
    else:
        print(f"{num:02}, ", end="")
