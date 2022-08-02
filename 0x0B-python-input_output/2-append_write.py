#!/usr/bin/python3
'''This module contains a function that appends to a file'''


def append_write(filename="", text=""):
    '''This function appends to a file'''
    with open(filename, 'a', encoding="utf-8") as aFile2:
        return(aFile2.write(text))


if __name__ == "__main__":
    append_write(filename, text)
