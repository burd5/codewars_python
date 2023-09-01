# Difference Between Two Collections

"""
Find the difference between two collections. The difference means that either the character is present in one collection or it is present in other, but not in both. Return a sorted list with the difference.

The collections can contain any character and can contain duplicates.

Example
A = [a, a, t, e, f, i, j]

B = [t, g, g, i, k, f]

difference = [a, e, g, j, k]

"""


# My Solution

def diff(a, b):
    if not a: return b
    if not b: return a
    return sorted(list(set(a) - set(b)) + list(set(b) - set(a)))

# Other Solutions

def diff(a, b):
    # is the "symmetric difference" operator. It returns a set of whatever items are unique to either set.
    return sorted(set(a) ^ set(b))

def diff(a, b):
    return sorted(set(a).symmetric_difference(b))

# return a sorted set with the difference
def diff(a, b):
  a = set(a)
  b = set(b)
  c = a.symmetric_difference(b)
  return sorted(list(c))