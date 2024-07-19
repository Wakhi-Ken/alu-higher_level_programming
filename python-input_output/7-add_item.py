#!/usr/bin/python3
"""
all arguments to a python list and saves to a json file
"""

import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    try:
        args = load_from_json_file("add_item.json")
    except FileNotFoundError:
        args = []
    args.extend(sys.argv[1:])
    save_to_json_file(args, "add_item.json")
