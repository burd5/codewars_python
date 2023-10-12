# Lowest Product of 4 Consecutive Numbers

"""
Create a function that returns the lowest product of 4 consecutive digits in a number given as a string.

This should only work if the number has 4 digits or more. If not, return "Number is too small".

Example
lowest_product("123456789") --> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"

"""

# My Solution

import numpy as np

def lowest_product(input):
    if len(input) < 4: return 'Number is too small'

    products = []
    
    for i in range(len(input) - 3):
        nums = np.prod([int(x) for x in input[i: i + 4]])
        products.append(nums)
        
    return min(products)


# Other Solutions

def lowest_product(input):
    length = len(input)
    
    if length < 4:
        return "Number is too small"
    
    def muller(fourchar):
        prod = 1
        for num in fourchar:
            prod *= int(num)
        return prod
        
    return min([muller(input[i:i+4]) for i in range(length-3)])

# # #

from operator import mul
from functools import reduce # python 3 support

def lowest_product(input):
    if len(input) < 4: return "Number is too small"
    return min([reduce(mul, map(int, input[i:i+4])) for i in range(len(input)-3)])