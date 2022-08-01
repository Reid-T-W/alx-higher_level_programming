#!/usr/bin/python3
'''This module includes a function that verifies if an object is an instace'''


def is_same_class(obj, a_class):
    '''This function check if an object is an instace of a class'''
    if (type(obj) is a_class):
        return True
    return False


if __name__ == "__main__":
    is_same_class(obj, a_class)
