# Merge Arrays

"""
You have two sorted arrays a and b, merge them to form new array of unique items.

If an item is present in both arrays, it should be part of the resulting array if and only if it appears in both arrays the same number of times.

Example
For a = [1, 3, 40, 40, 50, 60, 60, 60] and b = [2, 40, 40, 50, 50, 65], the result should be [1, 2, 3, 40, 60, 65].

"""

# my solution
def merge_arrays(a, b):
    c = a + b
    result = []
    for num in c:
        if num in result: pass
        elif num in a and num in b:
            if a.count(num) == b.count(num):
                result.append(num)
        else: result.append(num)
    return sorted(result)

# similar solution

def merge_arrays(a, b):
    out = []
    for n in a+b:
        if n in a and n in b:
            if a.count(n) == b.count(n):
                out.append(n)
        else:
            out.append(n)
    return sorted(set(out))