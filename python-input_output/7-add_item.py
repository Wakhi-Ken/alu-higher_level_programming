#!/usr/bin/python3
"""Saves command line arguments to a file."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""a script that adds all arguments to a Python list
"""
try:
    args = load_from_json_file("add_item.json")
except FileNotFoundError:
    args = []
args.extend(sys.argv[1:])
save_to_json_file(args, "add_item.json")
