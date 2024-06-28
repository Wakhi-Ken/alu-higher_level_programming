#!/usr/bin/python3
i = 0
while i < 100:
    print(f"{i:02d}", end=", " if i != 99 else "\n")
    i += 1
