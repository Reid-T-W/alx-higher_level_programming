#!/usr/bin/python3
'''This module includes a function that checks for subclass'''


def inherits_from(obj, a_class):
    '''This function checks if an object is a subclass'''
    if (issubclass(type(obj), a_class) and type(obj) is not a_class):
        return (True)
    return (False)


if __name__ == "__main__":
    inherits_from(obj, a_class)
