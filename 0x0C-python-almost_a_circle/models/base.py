#!/usr/bin/python3
'''This module contains the base class'''
import json
from os.path import exists


class Base:
    '''This class contains the Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization method'''
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.__id = Base.__nb_objects

    @property
    def id(self):
        '''id getter'''
        return self.__id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''static method to_json_string'''
        if ((list_dictionaries is None) or (len(list_dictionaries) == 0)):
            return("[]")
        return(json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''static method from_json_string'''
        if ((json_string is None) or (len(json_string) == 0)):
            return []
        return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        '''class method save_to_file'''
        dict_obj_list = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as wFile:
            if ((list_objs is None) or (len(list_objs) == 0)):
                wFile.write(Base.to_json_string([]))
            else:
                for obj in list_objs:
                    dict_obj = obj.to_dictionary()
                    dict_obj_list.append(dict_obj)
                wFile.write(Base.to_json_string(dict_obj_list))

    @classmethod
    def create(cls, **dictionary):
        '''class method create'''
        kwargs = {}
        if (cls.__name__ == "Rectangle"):
            dummy = cls(11, 13)
            if ('x' in dictionary):
                kwargs['x'] = dictionary['x']
            if ('y' in dictionary):
                kwargs['y'] = dictionary['y']
            if ('width' in dictionary):
                kwargs['width'] = dictionary['width']
            if ('height' in dictionary):
                kwargs['height'] = dictionary['height']
            if ('id' in dictionary):
                kwargs['id'] = dictionary['id']
            dummy.update(**kwargs)
        elif (cls.__name__ == "Square"):
            dummy = cls(11)
            if ('x' in dictionary):
                kwargs['x'] = dictionary['x']
            if ('y' in dictionary):
                kwargs['y'] = dictionary['y']
            if ('size' in dictionary):
                kwargs['size'] = dictionary['size']
            if ('id' in dictionary):
                kwargs['id'] = dictionary['id']
            dummy.update(**kwargs)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''class method load_from_file'''
        instance_list = []
        filename = cls.__name__ + ".json"
        if (exists(filename) is True):
            with open(filename, 'r', encoding="utf-8") as rFile:
                dict_list = Base.from_json_string(rFile.read())
                for item in dict_list:
                    instance_list.append(cls.create(**item))
                return (instance_list)
        else:
            return ([])
