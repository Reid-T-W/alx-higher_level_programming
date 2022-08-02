#!/usr/bin/python3
'''This script adds arguments to a json file'''
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
empty = 0
prev_list = []

if (os.path.exists("add_item.json")):
    prev_list = load_from_json_file("add_item.json")
    for arg in args[1:]:
        prev_list.append(arg)
    save_to_json_file(prev_list, "add_item.json")
else:
    save_to_json_file(args[1:], "add_item.json")
