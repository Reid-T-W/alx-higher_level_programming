#!/usr/bin/python3
'''Module that contains a function that checks if an object is an instance'''


def is_kind_of_class(obj, a_class):
    '''Function that check if an object is an instance'''
    return (isinstance(obj, a_class))


if __name__ == "__main__":
    is_kind_of_class(obj, a_class)
