# Very Even Numbers

"""
Write a function that returns true if the number is a "Very Even" number.

If a number is a single digit, then it is simply "Very Even" if it itself is even.

If it has 2 or more digits, it is "Very Even" if the sum of its digits is "Very Even".

Examples
number = 88 => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd 

number = 222 => returns true -> 2 + 2 + 2 = 6 => 6 is even

number = 5 => returns false

number = 841 => returns true -> 8 + 4 + 1 = 13 -> 1 + 3 => 4 is even

"""
# My Solution

def is_very_even_number(n):
    while len(str(n)) > 1:
        n = sum([int(x) for x in str(n)])
    if len(str(n)) == 1: return n % 2 == 0

# Other Solution

def is_very_even_number(n):
    while len(str(n)) > 1:
        n = sum(int(x) for x in str(n))
    return True if n % 2 == 0 else False