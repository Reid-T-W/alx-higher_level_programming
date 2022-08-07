#!/usr/bin/python3
'''This module contains a class that inherits from Rectangle'''
from models.rectangle import Rectangle

class Square(Rectangle):
    '''This class inherits from Rectangle class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(super().id, super().x, super().y, super().width)
