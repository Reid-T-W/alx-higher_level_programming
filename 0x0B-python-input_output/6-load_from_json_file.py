#!/usr/bin/python3
'''This module contains a function that creates an object from a json file'''
import json


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as rFile6:
        return(json.load(rFile6))


if __name__ == "__main__":
    load_from_json_file(filename)
