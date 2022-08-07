#!/usr/bin/python3
'''This module contains the base class'''


class Base:
    '''This class contains the Base class'''
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.__id = Base.__nb_objects
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
