#!/usr/bin/python3
'''This module contains a function that writes json to file'''
import json


def save_to_json_file(my_obj, filename):
    '''This function writes json to file'''
    json_format = json.dumps(my_obj)
    with open(filename, 'a', encoding="utf-8") as wFile5:
        wFile5.write(json_format)


if __name__ == "__main__":
    save_to_json_file(my_obj, filename)
