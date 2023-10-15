# Find Factors Down to Limit

"""
In this Kata you have to find the factors of integer down to the limit including the limiting number. There will be no negative numbers. Return the result as an array of numbers in ascending order.

If the limit is more than the integer, return an empty list

As a challenge, see if you can do it in one line

"""


# My Solution

def factors(integer, limit):
    return [x for x in range(limit, integer + 1) if integer % x == 0]