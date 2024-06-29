#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    answer = len(my_list) - 1
    if idx > answer or idx < 0:
        return my_list
    new_list = my_list
    del new_list[idx]
    return new_list
