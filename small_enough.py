# Code Wars 7kyu - Small Enough?

"""

You will be given an array (a) and a limit value (limit). You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.

Do not use loops. Do not modify input array.

"""

# My Solution

def small_enough(a, limit):
    return len(a) == len(list(filter(lambda x:x <= limit, a)))

# Simple Solution Using Max

def small_enough(a, limit): 
    return max(a) <= limit