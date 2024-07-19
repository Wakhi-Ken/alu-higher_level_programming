#!/usr/bin/python3
""" write_file() function."""


def write_file(filename="", text=""):
    """writes a string to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
    return 0
