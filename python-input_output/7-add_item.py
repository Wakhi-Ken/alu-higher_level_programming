#!/usr/bin/python3
"""Saves command line arguments to a file."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""a script that adds all arguments to a Python list
"""
try:
    """Load existing arguments from the JSON file"""
    args = load_from_json_file("add_item.json")
except FileNotFoundError:
    """If the file doesn't exist, initialize with an empty list"""
    args = []

"""Append the command line arguments to the list"""
args.extend(sys.argv[1:])
"""Save the updated list to the JSON file"""
save_to_json_file(args, "add_item.json")
