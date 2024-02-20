# Consecutive Items

"""

You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).

It is guaranteed that a and b are both present in arr.

"""

# My Solution

def consecutive(arr, a, b):
    for i in range(len(arr)-1):
        if set([a,b]) == set(arr[i:i+2]):
            return True
    
    return False

# Other Solutions

def consecutive(A, a, b):
    return abs(A.index(a)-A.index(b))==1

def consecutive(arr, a, b):
    x = arr.index(a)
    y = arr.index(b)
    return abs(x-y)==1

#