# Longest Sequence with Zero Sum

"""
Write a method that takes an array of signed integers, and returns the longest contiguous subsequence of this array that has a total sum of elements of exactly 0.

If more than one equally long subsequences have a zero sum, return the one starting at the highest index.

For example:
maxZeroSequenceLength([25, -35, 12, 6, 92, -115, 17, 2, 2, 2, -7, 2, -9, 16, 2, -11]) should return
[92, -115, 17, 2, 2, 2], because this is the longest zero-sum sequence in the array.

"""

# My Solution

def max_zero_sequence(arr): 
    longest = 0
    sub_array = []
    
    # loop through entire array and sum sub-arrays, move left pointer once right hits end
    for i in range(0, len(arr) + 1):
        for j in range(0, len(arr) + 1):
            total = sum(arr[i:j])
            if total == 0:
                if len(arr[i:j]) >= longest:
                    sub_array = arr[i:j]
                    longest = len(arr[i:j])
    return sub_array

# Other Solutions

from itertools import accumulate

def max_zero_sequence(arr):
    memo, start, stop = {0: 0}, 0, 0
    for i, x in enumerate(accumulate(arr), 1):
        if x in memo:
            if start + i > stop + memo[x]:
                start, stop = memo[x], i
        else:
            memo[x] = i
    return arr[start:stop]

def max_zero_sequence(arr: list) -> list:
    aux = {0: 0}
    acc = 0
    res = []
    for i, x in enumerate(arr, 1):
        acc += x
        if acc not in aux:
            aux[acc] = i
        elif len(res) < i - aux[acc]:
            res = arr[aux[acc]:i]
    return res
