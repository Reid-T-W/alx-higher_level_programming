#!/usr/bin/python3
def pow(a, b):
    value = 1
    if (b >= 0):
        for i in range(b):
            value = value * a
        return value
    elif (b < 0):
        b = -1 * b
        for i in range(b):
            value = value * a
        return (1 / value)
