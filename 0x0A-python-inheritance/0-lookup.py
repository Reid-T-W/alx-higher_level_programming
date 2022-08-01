#!/usr/bin/python3
'''This module defines a lookup function for object attribute and methods'''


def lookup(obj):
    '''This function returns the attributes and methods of an object'''
    return dir(obj)


if __name__ == "__main__":
    lookup(obj)
