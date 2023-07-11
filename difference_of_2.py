# Difference of 2 - Codewars 6kyu

"""
The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

The result array should be sorted in ascending order of values.

Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

Examples
[1, 2, 3, 4]  should return [(1, 3), (2, 4)]

[4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

[1, 23, 3, 4, 7] should return [(1, 3)]

[4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]

"""

# My solution

def twos_difference(lst): 
    pairs = []
    new_list = sorted(lst)
    for num in new_list:
        if num + 2 in new_list:
            pair = (num, num + 2)
            if pair not in pairs:
                pairs.append(pair)
    return pairs

# Quicker Solution - List Comprehension

def twos_difference(a):
    s = set(a)
    return sorted((x, x + 2) for x in a if x + 2 in s)

