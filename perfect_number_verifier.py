# Perfect Number Verifier

"""
A perfect number is a number in which the sum of its divisors (excluding itself) are equal to itself.

Write a function that can verify if the given integer n is a perfect number, and return True if it is, or return False if not.

Examples
n = 28 has the following divisors: 1, 2, 4, 7, 14, 28

1 + 2 + 4 + 7 + 14 = 28 therefore 28 is a perfect number, so you should return True

Another example:

n = 25 has the following divisors: 1, 5, 25

1 + 5 = 6 therefore 25 is not a perfect number, so you should return False
"""

# Solutions

def isPerfect(n):
    return n in [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]

#### 

def divisors(n):
    d = {1, n}
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            d.add(k)
            d.add(n//k)
    d.remove(n)
    return d


def is_perfect(n):
    return sum(divisors(n)) == n
# Multiple Solutions that Timed Out

def is_perfect(n):
    return n == sum([x for x in range(1, n) if n % x == 0])

def is_perfect(n):
    sum_total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum_total += i
        if sum_total > n:
            return False
    return sum_total == n



