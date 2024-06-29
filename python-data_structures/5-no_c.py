#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    result = ""
    for chare in range(length):
        old = my_string[chare]
        if old == 'c' or old == 'C':
            new = ""
            result += new
        else:
            result += old
    return result
