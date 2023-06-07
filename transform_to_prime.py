# Transform to Prime - Codewars 6kyu

"""
Given a List [] of n integers , find minimum number to be inserted in a list, so that sum of all elements of list should equal the closest prime number .

Notes
List size is at least 2 .

List's numbers will only positives (n > 0) .

Repetition of numbers in the list could occur .

The newer list's sum should equal the closest prime number .

"""

# To-Do List

"""
1. Find current sum of integer list
2. Find closest prime number to that sum

"""
# finds if numbers are prime
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

# Function to difference of next prime - current sum
def minimum_number(numbers):
    curr_sum = sum(numbers)
    if is_prime(curr_sum): return 0
    next_prime = None
    i = curr_sum + 1
    while next_prime == None:
        isPrime = is_prime(i)
        if isPrime: 
            next_prime = i
        i += 1
    return next_prime - curr_sum