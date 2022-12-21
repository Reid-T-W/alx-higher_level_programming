#!/usr/bin/python3
"""Empty class"""


class Square():
    """Empty square class"""
    def __init__(self, size=0):
        """called on initialization"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area of the square"""
        return(self.__size * self.__size)
