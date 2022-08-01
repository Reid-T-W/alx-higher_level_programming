#!/usr/bin/python3
'''Module that creates a class with a method that raises an exception'''


class BaseGeometry():
    '''Class with method that raises an exception'''
    def area(self):
        '''Function that raises an exception'''
        raise Exception("area() is not implemented")
