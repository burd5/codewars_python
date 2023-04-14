"""
Mash 2 arrays together so that the returning array has alternating elements of the 2 arrays . Both arrays will always be the same length.

eg. [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']

"""

# my solution

def array_mash(a, b):
    arr = []
    for i in range(len(a)):
        arr.extend([a[i], b[i]])
        
    return arr

# one liner

def array_mash(xs, ys):
    return [z for p in zip(xs, ys) for z in p]