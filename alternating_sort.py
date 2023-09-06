# Alternating Sort

"""
that combines the elements of an array by sorting the elements ascending by their absolute value and outputs negative and non-negative integers alternatingly (starting with the negative value, if any).

E.g.

alternate_sort([5, -42, 2, -3, -4, 8, -9,]) == [-3, 2, -4, 5, -9, 8, -42]
alternate_sort([5, -42, 2, -3, -4, 8, 9]) == [-3, 2, -4, 5, -42, 8, 9]
alternate_sort([5, 2, -3, -4, 8, -9]) == [-3, 2, -4, 5, -9, 8]
alternate_sort([5, 2, 9, 3, 8, 4]) == [2, 3, 4, 5, 8, 9]

"""

# My Solution

def alternate_sort(l):
    # list for all negative values, sorted by abs value
    negative = sorted([x for x in l if x < 0], key=lambda x:abs(x))
    
    # list for all positive values, sorted
    positive = sorted([x for x in l if x >= 0])
    
    # list to hold sorted values
    alternate = []
    
    # loop to alternate adding these values, starting with negative
    while negative or positive:
        if negative:
            alternate.append(negative.pop(0))
        if positive:
            alternate.append(positive.pop(0))
    
    # return sorted list
    return alternate

# Other Solutions

from itertools import chain, zip_longest

def alternate_sort(l):
    l=sorted(l,key=abs)
    p,n=[n for n in l if n>=0],[n for n in l if n<0]
    return [n for n in chain(*zip_longest(n,p)) if n is not None]