#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_characters = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
                 }

    full_tal = 0
    prev_hashtag = 0

    for char in reversed(roman_string):
        val = roman_characters[char]
        full_tal += val if val >= prev_hashtag else -val
        prev_hashtag = val

    return full_tal
