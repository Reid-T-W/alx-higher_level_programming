#!/usr/bin/python3
'''This module contains the base class'''
import json
import csv
from os.path import exists
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''class method save to csv'''
        dict_obj_list = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', encoding="utf-8") as f:
            if ((list_objs is None) or (len(list_objs) == 0)):
                write_csv = csv.writer(f)
                write_csv.writerow(list_objs)
            else:
                for obj in list_objs:
                    dict_obj = obj.to_dictionary()
                    dict_obj_list.append(dict_obj)
                write_csv = csv.writer(f)
                write_csv.writerow(dict_obj_list)

    @classmethod
    def load_from_file_csv(cls):
        '''class method to load from csv'''
        instance_list = []
        filename = cls.__name__ + ".csv"
        if (exists(filename) is True):
            with open(filename, 'r', encoding="utf-8") as f:
                read_csv = csv.reader(f)
                for row in read_csv:
                    dict_list = row
                print(dict_list)
                for item in dict_list:
                    instance_list.append(cls.create(**item))
                return (instance_list)
        else:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        bob = turtle.Turtle()
        if (list_rectangles is not None):
            for inst_rect in list_rectangles:
                obj_rect = inst_rect

                bob.color("black", "orange")
                bob.penup()
                bob.setx(obj_rect.x)
                bob.sety(obj_rect.y)
                bob.pendown()
                bob.begin_fill()
                bob.forward(obj_rect.width)
                bob.right(90)
                bob.forward(obj_rect.height)
                bob.right(90)
                bob.forward(obj_rect.width)
                bob.right(90)
                bob.forward(obj_rect.height)
                bob.end_fill()

        if (list_squares is not None):
            for inst_square in list_squares:
                obj_square = inst_square

                bob.color("blue", "cyan")
                bob.penup()
                bob.setx(obj_square.x)
                bob.sety(obj_square.y)
                bob.pendown()
                bob.begin_fill()
                bob.forward(obj_square.size)
                bob.right(90)
                bob.forward(obj_square.size)
                bob.right(90)
                bob.forward(obj_square.size)
                bob.right(90)
                bob.forward(obj_square.size)
                bob.end_fill()

        turtle.done()
