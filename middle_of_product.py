"""
Given a string of characters, I want the function findMiddle()/find_middle() to return the middle number in the product of each digit in the string.

Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.

Not all strings will contain digits. In this case and the case for any non-strings, return -1.

If the product has an even number of digits, return the middle two digits

Example: 1563 -> 56

NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. Example 2016 -> 1

"""

# my attempt

import re
import math

def find_middle(string):
    if not string or list(string) == string: return -1
    num_sum = 1
    for val in string:
        if val.isdigit():
            num_sum *= int(val)
    num_sum = str(num_sum)
    mid = math.floor(len(num_sum)/2)
    if mid == 0: return -1
    return int(num_sum[mid]) if len(num_sum) % 2 != 0 else int(num_sum[mid - 1: mid +1])

# solution

from operator import mul
from functools import reduce

def find_middle(s):
    if not s or not isinstance(s,str): return -1
    
    lstDig = [int(c) for c in s if c.isnumeric()]
    if not lstDig: return -1
    
    prod = str( reduce(mul,lstDig) )
    i    = (len(prod) - 1) // 2
    return int(prod[i:-i or len(prod)])

# try except

from functools import reduce
from operator import mul

def find_middle(string):
    try:
        s = str(reduce(mul, map(int, filter(str.isdigit, string))))
        q, r = divmod(len(s), 2)
        return int(s[q+r-1:q+1])
    except TypeError:
        return -1