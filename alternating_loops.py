# Alternating Loops - 6kyu

"""
Write

function combine()
that combines arrays by alternatingly taking elements passed to it.

E.g

combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
Arrays can have different lengths.

"""
# my solution

from itertools import chain, zip_longest
def combine(*args):
    return [x for x in chain.from_iterable(zip_longest(*args)) if x is not None]

# other solution

def combine(*args):
  out = list()
  for i in range(len(max(args, key=len))): #Sometimes you just have to love python
    for arr in args:
      if i < len(arr): out.append(arr[i])
  return out