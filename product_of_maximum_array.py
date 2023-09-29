# Product of Maximum Array

"""
Task
Given an array/list [] of integers , Find the product of the k maximal numbers.

Notes
Array/list size is at least 3 .

Array/list's numbers Will be mixture of positives , negatives and zeros

Repetition of numbers in the array/list could occur.

Input >> Output Examples
maxProduct ({4, 3, 5}, 2) ==>  return (20)
Explanation:
Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima is 5 * 4 = 20 .

"""

# My Solution

def max_product(lst, n_largest_elements):
    numbers = sorted(lst)[-(n_largest_elements):]
    
    product = 1
    
    for num in numbers:
        product *= num
        
    return product

# Other Solutions

from functools import reduce
from operator import mul
from heapq import nlargest

def maxProduct (lst, n):
    return reduce(mul, nlargest(n, lst))



