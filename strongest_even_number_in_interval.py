# Strongest Even Number in an Interval

"""
A strongness of an even number is the number of times we can successively divide by 2 until we reach an odd number starting with an even number n.

For example, if n = 12, then

12 / 2 = 6
6 / 2 = 3
So we divided successively 2 times and we reached 3, so the strongness of 12 is 2.

If n = 16 then

16 / 2 = 8
8 / 2 = 4
4 / 2 = 2
2 / 2 = 1
we divided successively 4 times and we reached 1, so the strongness of 16 is 4

Task
Given a closed interval [n, m], return the even number that is the strongest in the interval. If multiple solutions exist return the smallest strongest even number.

Note that programs must run within the allotted server time; a naive solution will probably time out.

"""

# Solutions

def strongest_even(n, m):
    while m & m - 1 >= n:
        m &= m - 1
    return m


from math import log2

def strongest_even(n, m):
    """Returns the strongest even number in the set of integers on interval
       [n, m].
    """

    #It can be shown that the largest power of 2 on an interval [n, m] will
    #necessarily be the strongest even number. Check first if the interval
    #contains a power of 2, by comparing the log2 of the endpoints.
    if int(log2(m)) > int(log2(n)):
        return 2**int(log2(m))

    #Modify the endpoints exclude any odd numbers. If the two endpoints are
    #equal, the original interval contains only a single even number. Return it.
    n += n % 2
    m -= m % 2
    if n == m:
        return n

    #All optimizations and edge cases are exhausted. Recurse with the
    #modified endpoints halved, and multiply the result by 2.