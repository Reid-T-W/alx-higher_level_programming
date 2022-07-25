#!/usr/bin/python3
'''This module defines a rectangle with private instance variables'''


class Rectangle:
    '''This class defines a rectangle'''
    def __init__(self, width=0, height=0):
        '''Instantiation with optional width and height'''
        self.height = height
        self.width = width

    @property
    def height(self):
        '''width Getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''width Setter'''
        if (type(value) == int):
            if (value > 0):
                self.__height = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def width(self):
        '''height getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''height setter'''
        if (type(value) == int):
            if (value > 0):
                self.__width = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
