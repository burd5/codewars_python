# Possibilities Array

"""
A non-empty array a of length n is called an array of all possibilities if it contains all numbers between 0 and a.length - 1 (both inclusive).

Write a method named IsAllPossibilities/isAllPossibilities/is_all_possibilities that accepts an integer array and returns true if the array is an array of all possibilities, else false.

Examples:

[1,2,0,3] => True
# Includes all numbers between 0 and a.length - 1 (4 - 1 = 3)

[0,1,2,2,3] => False
# Doesn't include all numbers between 0 and a.length - 1 (5 - 1 = 4)

[0] => True
# Includes all numbers between 0 and a.length - 1 (1 - 1 = 0).

"""

# My Solution

def is_all_possibilities(arr):
    return sorted(arr) == [i for i in range(0, len(arr))]

# Simpler Solution

def is_all_possibilities(arr):
    for i in range(0, len(arr)):
        if i not in arr:
            return False
    return True