#!/usr/bin/python3
tens = 0
while tens < 10:
    ones = tens + 1
    while ones < 10:
        if not (tens * 10 + ones) == 89:
            print("{:d}{:d}, ".format(tens, ones), end="")
        else:
            print("{:d}{:d}".format(tens, ones), end="\n")
        ones += 1
    tens += 1
