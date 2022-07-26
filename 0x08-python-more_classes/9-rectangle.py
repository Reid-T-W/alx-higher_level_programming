#!/usr/bin/python3
'''This module defines a rectangle with private instance variables'''


class Rectangle:
    '''This class defines a rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Instantiation with optional width and height'''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __repr__(self):
        '''__retr__'''
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __str__(self):
        '''__str___'''
        shape = ""
        if (self.__height == 0 or self.__width == 0):
            return shape
        for row in range(self.__height):
            for col in range(self.__width):
                shape += str(self.print_symbol)
            if (row != self.height - 1):
                shape += "\n"
        return shape

    def __del__(self):
        '''__del___'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def height(self):
        '''height Getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height Setter'''
        if (isinstance(value, int)):
            if (value >= 0):
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if (isinstance(value, int)):
            if (value >= 0):
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if (self.__height == 0 or self.__width == 0):
            return 0

        return((2 * self.__height) + (2 * self.__width))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if (rect_1.area() > rect_2.area()):
            return rect_1
        elif (rect_1.area() == rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
