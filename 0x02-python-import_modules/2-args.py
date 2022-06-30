#!/usr/bin/python3
import sys


def main():
    len_argv = len(sys.argv)
    print(len_argv - 1, end=" ")
    if (len_argv == 2):
        print("argument:")
    elif (len_argv > 2):
        print("arguments:")
    elif (len_argv == 1):
        print("arguments.")
    if (len_argv > 1):
        for i in range(1, len_argv):
            print("{:d}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
