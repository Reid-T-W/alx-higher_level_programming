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
        '''height Getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height Setter'''
        if (isinstance(value, int)):
            if (value >= 0):
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if (isinstance(value, int)):
            if (value >= 0):
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__height == 0 or self.__width == 0):
            return 0

        return((2 * self.__height) + (2 * self.__width))
