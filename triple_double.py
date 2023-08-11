# Triple Double - Codewars 6kyu

"""
Write a function

triple_double(num1, num2)
which takes numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.

If this isn't the case, return 0

Examples
triple_double(451999277, 41177722899) == 1
# num1 has straight triple 999s and num2 has straight double 99s

triple_double(1222345, 12345) == 0
# num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1

"""

import re

def triple_double(num1, num2):
    num1,num2 = str(num1), str(num2)
    num1_triples = re.findall(r"(\d)\1\1", num1)
    return 0 if not num1_triples else ''.join(num1_triples * 2) in num2

# Other Solutions

def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])

def triple_double(num1, num2):
    for x in range(10):
        if str(x) * 3 in str(num1):
            if str(x) * 2 in str(num2):
                return 1
    return 0