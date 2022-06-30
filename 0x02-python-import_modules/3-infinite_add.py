#!/usr/bin/python3
import sys


def main():
    sum = 0
    if (len(sys.argv) == 1):
        print("{:d}".format(0))
    elif (len(sys.argv) > 1):
        for i in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[i])
        print(sum)


if __name__ == "__main__":
    main()
