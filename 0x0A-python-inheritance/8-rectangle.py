#!/usr/bin/python3
'''Module that creates a class with a method that raises an exception'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class with method that raises an exception'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
