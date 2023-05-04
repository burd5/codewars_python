"""
Given an array, return the difference between the count of even numbers and the 
count of odd numbers. 0 will be considered an even number.

For example:
solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. 
Even - Odd = 2 - 2 = 0.  Let's now add two letters to the last example:

solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters.

"""

# my solution

def solve(a):
    odds = [x for x in a if isinstance(x, int) and x % 2 != 0]
    even = [x for x in a if isinstance(x, int) and x % 2 == 0]
    return len(even) - len(odds)

# other solution using sum

def solve(a):
    return sum(1 if v % 2 == 0 else -1 for v in a if type(v) == int)