#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        raise ValueError("Input should be a single character")
    if ('a' <= c <= 'z'):
        return True
    else:
        return False
