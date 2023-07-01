# Count and Group Character Occurences in String

"""
Write a method that takes a string as an argument and groups the number of time each character appears in the string as a hash sorted by the highest number of occurrences.

The characters should be sorted alphabetically e.g:

get_char_count("cba") == {1: ["a", "b", "c"]}
You should ignore spaces, special characters and count uppercase letters as lowercase ones.

For example:

get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]}

"""

# My Solution

def get_char_count(s):
    dict_ = {}
    s = s.lower()
    for val in s:
        if val.isalnum():
            counter = s.count(val)
            if counter in dict_:
                if val not in dict_[counter]:
                    dict_[counter].append(val)
                    dict_[counter] = sorted(dict_[counter])
            else:
                dict_[counter] = [val]
    dict_ = dict(sorted(dict_.items(), key=lambda item:item[0], reverse = True))
    return dict_

# Other Solutions

def get_char_count(s):
    counts = {}
    for c in (c.lower() for c in s if c.isalnum()):
        counts[c] = counts[c] + 1 if c in counts else 1
    m = {}
    for k, v in counts.items():
        m[v] = sorted(m[v] + [k]) if v in m else [k]
    return m

from collections import Counter, defaultdict
def get_char_count(s):
    d = defaultdict(list)
    c = Counter(sorted(s.lower()))
    for i,j in c.items():
        if i.isalnum() : d[j].append(i)
    return dict(sorted(d.items())[::-1])