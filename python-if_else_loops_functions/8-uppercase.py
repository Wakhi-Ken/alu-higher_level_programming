#!/usr/bin/python3
def uppercase(string):
    big = len(string)
    result = ""
    for char in range(big):
        ascii_v1 = ord(string[char])
        if 97 <= ascii_v1 <= 122:
            ascii_v2 = ascii_v1 - 32
            result += chr(ascii_v2)
        else:
            result += chr(ascii_v1)
    print("{}".format(result))
