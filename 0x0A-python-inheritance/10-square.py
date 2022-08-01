#!/usr/bin/python3
'''This module has a class that inherites from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("width", size)
        self.integer_validator("height", size)
        self.__size = size
        super().__init__(size, size)
