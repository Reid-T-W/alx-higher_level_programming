#!/usr/bin/python3
"""
This module adds two integers

...
Functions
---------
add_integer(a, b=98)
    Adds two integers
"""
def add_integer(a, b=98):
    """This function adds two integers
    If the argument b is not passed, a default value of 
    98 is used.

    Parameters
    ----------
    a : int
        first value
    b : int
        second value

    Raises
    ------
    TypeError
        If a and b are not int or float
    """
    if (not isinstance(a, int)):
        if (not isinstance(a, float)):
            raise TypeError('a must be an integer')
    if (not isinstance(b, int)):
        if (not isinstance(b, float)):
            raise TypeError('b must be an integer')

    if (isinstance(a, float)):
        a = int(a)
    if (isinstance(b, float)):
        b = int(b)
    return (a + b)
