#!/usr/bin/python3
'''This module contains the base class'''
import json
from os.path import exists


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if ((list_dictionaries is None) or (len(list_dictionaries) == 0)):
            return("[]")
        return(json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        if ((json_string is None) or (len(json_string) == 0)):
            return []
        return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding = "utf-8") as wFile:
            if ((list_objs is None) or (len(list_objs) == 0)):
                wFile.write(Base.to_json_string([]))
            else:
                for obj in list_objs:
                    dict_obj = obj.to_dictionary()
                    wFile.write(Base.to_json_string(dict_obj))

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(11, 13, 15)
        if (cls.__name__ == "Rectangle"):
            dummy.update(x=dictionary['x'], y=dictionary['y'], width=dictionary['width'], height=dictionary['height'], id=dictionary['id'])
        elif (cls.__name__ == "Square"):
            dummy.update(x=dictionary['x'], y=dictionary['y'], size=dictionary['size'], id=dictionary['id'])
        return dummy

    @classmethod
    def load_from_file(cls):
        instance_list = []
        from_file = []
        filename = cls.__name__ + ".json"
        if (exists(filename) is True):
            with open(filename, 'r', encoding = "utf-8") as rFile:
               from_file.append(rFile.read())
               json_string = Base.to_json_string(from_file)
               #print("From base class", from_file, "Type ",type(from_file))
               dict_list = Base.from_json_string(json_string)
               #print("From base class dict_list", dict_list, "Type ",type(dict_list))
               for item in dict_list:
                   instance_list.append(Base.create(**item))
               return (instance_list)
        else:
            return ([])
