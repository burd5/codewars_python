# Midpoint Sum

"""
Midpoint Sum
For a given list of integers, return the index of the element where the sums of the integers to the left and right of the current element are equal.

Ex:

ints = [4, 1, 7, 9, 3, 9]
# Since 4 + 1 + 7 = 12 and 3 + 9 = 12, the returned index would be 3

ints = [1, 0, -1]
# Returns None/nil/undefined/etc (depending on the language) as there
# are no indices where the left and right sums are equal

"""
# My Solution

def midpoint_sum(ints):
    if len(ints) <= 2: return None
    for i in range(1, len(ints) - 1):
        if sum(ints[:i]) == sum(ints[i + 1:]):
            return i
    return None
    
# Simpler Solution

def midpoint_sum(ints):
    for i in range(1,len(ints)-1):
        if sum(ints[:i])==sum(ints[i+1:]):return i