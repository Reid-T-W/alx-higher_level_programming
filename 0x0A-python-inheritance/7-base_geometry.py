#!/usr/bin/python3
'''Module that creates a class with a method that raises an exception'''


class BaseGeometry():
    '''Class with method that raises an exception'''
    def area(self):
        '''Function that raises an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Function that validates value'''
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
