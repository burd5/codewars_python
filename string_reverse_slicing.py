# Code Wars 7kyu - String Reverse Slicing

"""

"""
# My Solution
def reverse_slice(s):
    strs = []
    for i in range(len(s)):
        str = s[::-1]
        strs.append(str)
        s = s[:-1]
    return strs

# One Line Solution Using List Comprehension

def reverse_slice(a):
    return [a[i::-1] for i in range(len(a) - 1, -1, -1)]