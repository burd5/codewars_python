# Divide and Conquer (2)

"""
Create a function that takes a list of integers and a group length as parameters. Your task is to determine if it's possible to split all the numbers from the list into groups of the specified length, while ensuring that consecutive numbers are present within each group.

Input
lst: A list of integers representing the numbers to be divided into groups.

group_len: An integer indicating the desired length of each group.

Output
The function should return True if it's possible to create groups according to the criteria, and False otherwise.

Examples
consecutive_nums([1, 3, 5], 1) ➞ True
# It is always possible to create groups of length 1.

consecutive_nums([5, 6, 3, 4], 2) ➞ True
# Two groups of length 2: [3, 4], [5, 6]

consecutive_nums([1, 3, 4, 5], 2) ➞ False
# It is possible to make one group of length 2, but not a second one.

consecutive_nums([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) ➞ True
# [1, 2, 3], [2, 3, 4], [6, 7, 8]

consecutive_nums([1, 2, 3, 4, 5], 4) ➞ False
# The list length is not divisible by the group’s length.

"""

from collections import Counter

def consecutive_nums(lst, size):
    if len(lst)%size: return False

    cnt = Counter(lst)
    for v in sorted(cnt)[:-size+1 or None]:
        if not cnt[v]: continue
        n = cnt[v]
        for x in range(v,v+size):
            if cnt[x] < n: return False
            cnt[x] -= n
    return not sum(cnt.values())
