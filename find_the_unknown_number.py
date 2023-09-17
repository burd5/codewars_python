# Find the Unknown Number

"""
You are given three non-negative integers x,y,z. They represent the remainders of the unknown positive integer n divided by 3,5,7.

That is: n % 3 = x, n % 5 = y, n % 7 = z

Your task is to find the minimum possible positive integer n and return it.

Example
For x = 2, y = 3, z = 2, the output should be 23

23 % 3 = 2, 23 % 5 = 3, 23 % 7 = 2

For x = 1, y = 2, z = 3, the output should be 52

52 % 3 = 1, 52 % 5 = 2, 52 % 7 = 3

"""

# My Solution

def find_unknown_number(x,y,z):
    minimum = float('inf')
    for i in range(1000, 0, -1):
        x1 = i % 3
        y1 = i % 5
        z1 = i % 7 
        
        if x1 == x and y1 == y and z1 == z:
            if i < minimum: minimum = i
            
    return minimum

# Simplified Version of My Way

def find_unknown_number(x,y,z):
    for i in range(1,1000):
        if i%3 == x and i%5 == y and i%7 == z:
                return i

# Mathematical Way

def find_unknown_number(x,y,z):    
    return (x*70 + y*21 + z*15) % 105 or 105



