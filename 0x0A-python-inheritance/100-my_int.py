#!/usr/bin/python3
'''This module has a class that inherits from int'''


class MyInt(int):
    '''This class overrides two functions from int and exchanges them'''
    def __eq__(self, other):
        return(super().__ne__(other))

    def __ne__(self, other):
        return(super().__eq__(other))
