#!/usr/bin/python3
'''This module contains a class that inherits from Rectangle'''
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    '''This class inherits from Rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize Square'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return super().width

    @size.setter
    def size(self, size):
        '''size setter'''
        Rectangle.validate_type(size, "width")
        Rectangle.check_width_height(size, "width")
        self.width = size
        self.height = size

    def to_dictionary(self):
        '''to_dictionary method'''
        shape_dict = {}
        shape_dict["id"] = self.id
        shape_dict["x"] = self.x
        shape_dict["size"] = self.width
        shape_dict["y"] = self.y
        return shape_dict

    def __str__(self):
        '''__str__ method'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        '''update method'''
        if (len(args) != 0):
            id_arg = (args[0],)
            super().update(*id_arg)
            i = 0
            len_arg = len(args) - 1
            """
            if (i < len_arg):
                Base.id = args[1]
                i = i + 1
            """
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
            super().update(**kwargs)
            if ("size" in kwargs):
                self.width = kwargs['size']
                self.height = kwargs['size']
