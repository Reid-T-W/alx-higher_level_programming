#!/usr/bin/python3
'''This module contains a function that serializes objects into JSON'''
import json


def to_json_string(my_obj):
    '''This function serializes an object'''
    return(json.dumps(my_obj))


if __name__ == "__main__":
    to_json_string(my_obj)
