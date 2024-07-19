#!/usr/bin/python3
"""load_from_json_file() function."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON fie
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
