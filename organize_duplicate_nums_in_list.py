# Organize Duplicates Numbers in a List

"""
Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne.

Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. Subarrays should be in the same order as the first occurence of the number they contain:

group([3, 2, 6, 2, 1, 3])
>>> [[3, 3], [2, 2], [6], [1]]
Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.

"""

# My Solution

def group(arr):
    res = []
    seen = []
    for val in arr:
        if val not in seen:
            counter = arr.count(val)
            res.append([val] * counter)
        seen.append(val)
    return res

# One Line Answer

group=lambda arr: [[n]*arr.count(n) for n in sorted(set(arr), key=arr.index)]

# Other Solutions

def group(arr):
    st, res = set(arr), []
    for n in arr:
        if n in st:
            st.remove(n)
            res.append([n] * arr.count(n))
    return res

def group(arr):
    return [[n]*arr.count(n) for i, n in enumerate(arr) if arr.index(n) == i]
