#!/usr/bin/python3
'''This module defines a rectangle with private instance variables'''


class Rectangle():
    '''This class defines a rectangle'''
    def __init__(self, width = 0, height = 0):
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
        self.__height = value
    @property
    def width(self):
        '''height getter'''
        return self.__width
    @width.setter
    def width(self, value):
        '''height setter'''
        self.__width = value
