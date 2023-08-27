# Reverse Sublists of Even Numbers

"""
Write a function revSub which reverses all sublists where consecutive elements are even. Note that the odd numbers should remain where they are.

Example
With [1,2,4,5,9] as input, we should get [1,4,2,5,9]. Here, because [2,4] is a sublist of consecutive even numbers, it should be flipped. There could be more than one sublist of even numbers, or none at all.

A few other examples:

[] -> []
[2,4] -> [4,2]
[2,4,3] -> [4,2,3]
[2,4,3,10,2] -> [4,2,3,2,10]

"""


# My Solution

def rev_sub(arr):
    new_lst = []
    evens = []
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
        else:
            new_lst.extend(evens[::-1])
            new_lst.append(i)
            evens = []
    if evens: new_lst.extend(evens[::-1])
    return new_lst


# Other Solutions

from itertools import groupby
def rev_sub(arr):
    r = []
    for i in [list(g) for n,g in groupby(arr, key = lambda x : x%2)]:
        if i[0]%2:
            r += i
        else:
            r += i[::-1]
    return r