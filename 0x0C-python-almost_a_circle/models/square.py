#!/usr/bin/python3
'''This module contains a class that inherits from Rectangle'''
from models.rectangle import Rectangle
from models.base import Base

class Square(Rectangle):
    '''This class inherits from Rectangle class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return super().width
    
    @size.setter
    def size(self, size):
        Rectangle.validate_type(size, "width")
        Rectangle.check_width_height(size, "width")
        self.width = size
        self.height = size

    def to_dictionary(self):
        shape_dict = {}
        shape_dict["id"] = self.id
        shape_dict["x"] = self.x
        shape_dict["size"] = self.width
        shape_dict["y"] = self.y
        return shape_dict

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if (len(args) != 0):
            i = 0
            len_arg = len(args)
            if (i < len_arg):
                Base.id = args[0]
                i = i + 1
            if (i < len_arg):
                self.width = args[1]
                self.height = args[1]
                i = i + 1
            if (i < len_arg):
                self.x = args[2]
                i = i + 1
            if (i < len_arg):
                self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    Base.id = kwargs[key]
                else:
                    if (key == "size"):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == "x"):
                         self.x = kwargs[key]
                    elif (key == "y"):
                        self.y = kwargs[key]
