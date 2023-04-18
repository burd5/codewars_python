"""
Write a function that returns the greatest common factor of an array of positive integers. Your return value should be a number, you will only receive positive integers.

greatest_common_factor([46, 14, 20, 88]) # == 2

"""
# my solution

def greatest_common_factor(seq): 
    # find smallest number (which will be largest possible GCF)
    highest = min(seq) + 1
    GCF = 0
    # loop through range of 1 to smallest number, seeing if all numbers are divisible by current num
    for i in range(1, highest):
        if len([num for num in seq if num % i == 0]) == len(seq):
            GCF = i
    # return largest num
    return GCF

# other solutions using imported modules

from math import gcd
from functools import reduce

def greatest_common_factor(seq): 
    return reduce(gcd, seq)

greatest_common_factor = __import__('numpy').gcd.reduce


