#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()  # Use a set to store unique integers
    total_unique = 0

    for val in my_list:
        if val not in unique_numbers:
            total_unique += val
            unique_numbers.add(val)

    return total_unique
