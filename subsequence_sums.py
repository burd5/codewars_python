# Subsequence Sums

"""
Given a sequence of integers named arr, find the number of continuous subsequences (sublist or subarray) in arr that sum up to s. A continuous subsequence can be defined as a sequence inbetween a start index and stop index (inclusive) of the sequence. For instance, [2, 3, 4] is a continuous subsequence of [1, 2, 3, 4, 5] , but [3, 5] and [4, 1] are not.


arr = [1, 2, 3, -3, -2, -1], s = 0 -> 3 
# [3, -3], [2, 3, -3, -2], [1, 2, 3, -3, -2, -1]
------------------------------------------------------------
arr = [1, 5, -2, 4, 0, -7, -3, 6], s = 4 -> 4
# [1, 5, -2], [4], [4, 0], [1, 5, -2, 4, 0, -7, -3, 6]
------------------------------------------------------------
arr = [9, -2, -5, 8, 6, -10, 0, -4], s = -1 -> 2
# [-5, 8, 6, -10], [-5, 8, 6, -10, 0]

"""


# My Solution (Timed Out)

from itertools import accumulate
def subsequence_sums(arr, s):
    return sum(list(accumulate(arr[i:])).count(s) for i in range(len(arr)))


# Working solutions

from collections import defaultdict
from itertools import accumulate

def subsequence_sums(arr, s):
    res, memo = 0, defaultdict(int)
    for x in accumulate(arr, initial=0):
        res += memo[x-s]
        memo[x] += 1
    return res


from collections import defaultdict

def subsequence_sums(arr, s):
    sums_count = defaultdict(int)
    sums = 0
    count = 0
    for i in arr:
        sums += i
        if sums == s:
            count += 1
        if sums - s in sums_count:
            count += sums_count[sums - s]
        sums_count[sums] += 1
    return count