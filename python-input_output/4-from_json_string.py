#!/usr/bin/python3
"""from_json_string() function."""
import json


def from_json_string(my_str):
    """Deserializes a JSON string
    """
    return json.loads(my_str)
