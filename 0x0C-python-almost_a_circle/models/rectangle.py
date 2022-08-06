#!/usr/bin/python3
'''This module contains the rectangle class that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''This is a rectangle class that inherits from the Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        Rectangle.validate_type(width, "width")
        Rectangle.validate_type(height, "height")
        Rectangle.validate_type(x, "x")
        Rectangle.validate_type(y, "y")

        Rectangle.check_width_height(width, "width")
        Rectangle.check_width_height(height, "height")

        Rectangle.check_x_y(x, "x")
        Rectangle.check_x_y(y, "y")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        return __width

    @width.setter
    def width(self, width):
        Rectangle.validate_type(width, "width")
        Rectangle.check_width_height(width, "width")
        self.__width = width

    @property
    def height(self):
        return __height

    @height.setter
    def height(self, height):
        Rectangle.validate_type(height, "height")
        Rectangle.check_width_height(height, "height")
        self.__height = height

    @property
    def x(self):
        return __x

    @x.setter
    def x(self, x):
        Rectangle.validate_type(x, "x")
        Rectangle.check_x_y(x, "x")
        self.__x = x

    @property
    def y(self):
        return __y

    @y.setter
    def y(self, y):
        Rectangle.validate_type(y, "y")
        Rectangle.check_x_y(y, "y")
        self.__y = y
    
    def area(self):
        return(self.__width * self.__height)

    def display(self):
        for col in range(self.__height + self.__y):
            if col < self.__y:
                print()
            else:
                for row in range(self.__width + self.__x):
                    if row < (self.__x):
                        print(" ", end="")
                    else:
                        print('#', end="")
                print()

    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}/{}".format(super().id, self.__x, self.__y, self.__width, self.__height))


    @classmethod
    def validate_type(cls, value, caller):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(caller))
    
    @classmethod
    def check_width_height(cls, value, caller):
        if value <= 0:
            raise ValueError('{} must be > 0'.format(caller))
    
    @classmethod
    def check_x_y(cls, value, caller):
        if value < 0:
            raise ValueError('{} must be >= 0'.format(caller))
