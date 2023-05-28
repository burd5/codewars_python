"""
Your task in this kata is to implement a function that calculates the sum of the 
integers inside a string. For example, in the string 
"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the 
integers is 3635.

Note: only positive integers will be tested.
"""

# my solution

import re

def sum_of_integers_in_string(s):
    nums = re.findall("\d+", s)
    return sum([int(x) for x in nums])

# similar but more concise

import re

def sum_of_integers_in_string(s):
    return sum(int(x) for x in re.findall(r"(\d+)", s))

# other solution

import re

def sum_of_integers_in_string(s):
    return sum(map(int, re.findall("\d+", s)))