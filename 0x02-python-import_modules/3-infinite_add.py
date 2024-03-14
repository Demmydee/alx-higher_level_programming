#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number = len(sys.argv) - 1
    addarg = 0
    for num in range(number):
        addarg += int(sys.argv[num + 1])
    print("{}".format(addarg))
