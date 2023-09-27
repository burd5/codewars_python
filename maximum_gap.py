# Maximum Gap

"""
Given an array/list [] of integers , Find The maximum difference between the successive elements in its sorted form.

"""

# My Solution

def max_gap(numbers):
    numbers = sorted(numbers)
    return max(numbers[i] - numbers[i - 1] for i in range(1, len(numbers)))

# Other Solutions

def max_gap(numbers):
    lst = sorted(numbers)
    return max(b-a for a,b in zip(lst, lst[1:]))

import numpy

def max_gap(numbers):
    return max(numpy.diff(sorted(numbers)))