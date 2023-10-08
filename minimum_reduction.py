# Minimum Reduction

"""



"""


# Solutions

from bisect import bisect_left
from math import sqrt

def min_remove(xs):
    xs = sorted(xs)
    return min(bisect_left(xs, sqrt(x)) + nr for nr, x in enumerate(reversed(xs)))


#########

def min_remove(A):
    A.sort()
    right_pointer = 1
    left_pointer = 0
    while right_pointer < len(A):
        if A[left_pointer] ** 2 >= A[right_pointer]:
            right_pointer += 1
        else:
            left_pointer += 1
            right_pointer += 1
    return len(A) - right_pointer + left_pointer