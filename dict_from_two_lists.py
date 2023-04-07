"""
There are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values. Write a function createDict(keys, values) that returns a dictionary created from keys and values. If there are not enough values, the rest of keys should have a None (JS null)value. If there not enough keys, just ignore the rest of values.

Example 1:

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
Example 2:

keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}

"""

# my solution

def create_dict(keys, values):
    #
    dictionary =  dict.fromkeys(keys)
    #
    minimum = min(len(keys), len(values))
    #
    for i in range(minimum):
        dictionary[keys[i]] = values[i]
    #
    return dictionary

# similar but more elegant solution

def createDict(keys, values):  
    while len(keys) > len(values):
        values.append(None)
    dic = dict(zip(keys, values))
    return dic