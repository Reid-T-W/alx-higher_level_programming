#!/usr/bin/python3
'''This module contains a function that deserializes an object'''
import json


def from_json_string(my_str):
    '''This function deserializes an object'''
    return(json.loads(my_str))


if __name__ == "__main__":
    from_json_string(my_str)
