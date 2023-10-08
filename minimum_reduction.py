# Minimum Reduction

"""

Given an array of integers, find the minimum number of elements to remove from the array so that the square root of the largest integer in the array is less or equal to the smallest number in the same array.

x = smallest integer in the array

y = largest integer in the array

Find the minimum number of elements to remove so, √y ≤ x.

Example
A = [3, 6, 5, 9, 16]
min=3 max=16

√16 > 3

remove 16, so largest element becomes 9.

√9 ≤ 3

so

min_remove(A) = 1
since only 16 was removed.

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