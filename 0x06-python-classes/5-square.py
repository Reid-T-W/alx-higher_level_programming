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

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area of the square"""
        return(self.__size * self.__size)

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
        else:
            for col in range(self.__size):
                for row in range(self.__size):
                    print("#", end="")
                print()
