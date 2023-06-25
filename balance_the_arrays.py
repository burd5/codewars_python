# Balance the Arrays - Codewars 6kyu

"""
Check that the two provided arrays both contain the same number of different unique items, regardless of order. For example in the following:

[a,a,a,a,b,b] and [c,c,c,d,c,d]
Both arrays have four of one item and two of another, so balance should return true.

"""

# My solution

def balance(arr1, arr2):
    if len(arr1) != len(arr2): return False
    dict1 = {}
    dict2 = {}
    for i in range(len(arr1)):
        dict1[arr1[i]] = 1 + dict1.setdefault(arr1[i], 0)
        dict2[arr2[i]] = 1 + dict2.setdefault(arr2[i], 0)
    return sorted(dict1.values()) == sorted(dict2.values())

# solution using Counter module from collections

from collections import Counter

def balance(arr1, arr2):
    return sorted(Counter(arr1).values()) == sorted(Counter(arr2).values())