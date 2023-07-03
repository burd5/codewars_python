# Populate Hash with Array Keys and Default Values

"""
Complete the function so that it takes an array of keys and a default value and returns a hash (Ruby) / dictionary (Python) with all keys set to the default value.

Example
["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}

"""

# My Solution

def populate_dict(keys, default):
    dict = {}
    for k in keys:
        dict[k] = dict.setdefault(k, default)
    return dict

# One Liner

def populate_dict(keys, default):
    return {key: default for key in keys}