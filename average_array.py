"""
Create a function that takes a 2D array as an input, and outputs another array 
that contains the average values for the numbers in the nested arrays at the 
corresponding indexes.

Note: the function should also work with negative numbers and floats.

Examples
[ [1, 2, 3, 4], [5, 6, 7, 8] ]  ==>  [3, 4, 5, 6]

1st array: [1, 2, 3, 4]
2nd array: [5, 6, 7, 8]
            |  |  |  |
            v  v  v  v
average:   [3, 4, 5, 6]

"""

# my solution

def avg_array(arrs):
    sums = {}
    for arr in arrs:
        for i, val in enumerate(arr):
            if i in sums:
                sums[i] += val
            else:
                sums.setdefault(i, val)
        
    return [float(x/len(arrs)) for x in sums.values()]

# solution using zip

def avg_array(arrs):
    return [sum(a)/len(a) for a in zip(*arrs)]

# one liner

def avg_array(arrs):
    return [(sum(ar[i] for ar in arrs))/len(arrs) for i in range(len(arrs[0]))]