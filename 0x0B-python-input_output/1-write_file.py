#!/usr/bin/python3
'''This module contains a function that writes to a file'''


def write_file(filename="", text=""):
    '''This function writes to a file'''
    with open(filename, 'w', encoding="utf-8") as wFile_1:
        return(wFile_1.write(text))


if __name__ == "__main__":
    wirte_file(filename, text)
