"""
Change every letter in a given string to the next letter in the alphabet. The function takes a single parameter s (string).

Notes:

Spaces and special characters should remain the same.
Capital letters should transfer in the same way but remain capitilized.
Examples
"Hello"               -->  "Ifmmp"
"What is your name?"  -->  "Xibu jt zpvs obnf?"
"zoo"                 -->  "app"
"zzZAaa"              -->  "aaABbb"

"""

# my unneccesarily long solution

def next_letter(s):
    alph_lower = 'abcdefghijklmnopqrstuvwxyz'
    alph_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted_str = ''
    for i,letter in enumerate(s):
        if letter in alph_lower:
            letter_index = alph_lower.index(letter)
            if letter == alph_lower[-1]:
                converted_str += 'a'
            else: converted_str += alph_lower[letter_index + 1]
        elif letter in alph_upper:
            letter_index = alph_upper.index(letter)
            if letter == alph_upper[-1]:
                converted_str += 'A'
            else: converted_str += alph_upper[letter_index + 1]
        else:
            converted_str += letter
    return converted_str

# solution using translate

def next_letter(s):
    return s.translate(str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 
    'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA'))