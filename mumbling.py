# Codewars 7kyu - Mumbling

"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

"""

# My Solution

def accum(s):
    final_str = ''
    for i in range(len(s)):
        final_str += s[i].upper() + (s[i] * i).lower() + '-'
    return final_str[:-1]

# Clean Solution

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))