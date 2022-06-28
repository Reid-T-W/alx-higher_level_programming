#!/usr/bin/python3
def magic_calculation(a, b, c):
    if(b < a):
        return c
    elif(b > c):
        return(b + a)
    else:
        return(c - (a * b))
