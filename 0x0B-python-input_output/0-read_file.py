#!/usr/bin/python3
'''This module contains a function that reads from a file'''


def read_file(filename=""):
    '''This function reads a file'''
    with open(filename, encoding="utf-8") as file_0:
        print(file_0.read(), end="")


if __name__ == "__main__":
    read_file(filename)
