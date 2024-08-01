#!/usr/bin/python3
"""Defines a text_indentation function"""


def text_indentation(text):
    """text with 2 newlines after: '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special = {".", "?", ":"}
    begin = 0
    for end in range(len(text)):
        if text[end] in special:
            line = text[begin:end + 1] + "\n\n"
            begin = end + 1
            print("{}".format(line.strip(" ")), end="")
    if begin <= end:
        line = text[begin:end + 1]
        print("{}".format(line.strip(" ")), end="")
