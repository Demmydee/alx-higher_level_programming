#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))
    for num in range(number):
        print("{}: {}".format(num + 1, sys.argv[num + 1]))
