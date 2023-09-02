# Minimum Steps

"""
Given an array of N integers, you have to find how many times you have to add up the smallest numbers in the array until their Sum becomes greater or equal to K.

Notes:
List size is at least 3.

All numbers will be positive.

Numbers could occur more than once , (Duplications may exist).

Threshold K will always be reachable.

Input >> Output Examples
minimumSteps({1, 10, 12, 9, 2, 3}, 6)  ==>  return (2)

"""

# My Solution

def minimum_steps(numbers, value):
    # sort numbers
    numbers = sorted(numbers)
    
    # check to see if two lowest values already exceed given value
    if sum(numbers[:2]) > value: return 0

    # counter
    counter = 1
    curr_sum = sum(numbers[:2])
    i = 2
    
    # add next lowest value until conditions met
    while curr_sum < value:
        curr_sum += numbers[i]
        counter += 1
        i += 1
        
    return counter

# Simple Solution

def minimum_steps(arr, n):
    arr = sorted(arr)
    s = 0
    for i,v in enumerate(arr): 
        s += v
        if s >= n: return i