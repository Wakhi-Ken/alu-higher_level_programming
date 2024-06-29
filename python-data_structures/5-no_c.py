#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for chare in my_string:
        if chare != 'c' and chare != 'C':
            result += chare
            return result
