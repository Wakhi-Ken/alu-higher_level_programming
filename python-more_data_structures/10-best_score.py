#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    final = float('-inf')

    for key, val in a_dictionary.items():
        if val > final:
            final = val
            best_key = key

    return best_key
