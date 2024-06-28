#!/usr/bin/python3
i = 0
while i < 100:
    if i < 99:
        print(f"{i:02d}, ", end="")
    else:
        print(f"{i:02d}")
    i += 1
