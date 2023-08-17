# Scramblies

"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""

# My Solution

def scramble(s1, s2):
    # create dict to hold char value counts
    dict1 = {}
    dict2 = {}
    # loop to add characters from bigger string to dict
    for i in s1:
        dict1[i] = 1 + dict1.setdefault(i, 0)
        
    # loop through smaller string and check to see if char/val count are adequate
    for i in s2:
        dict2[i] = 1 + dict2.setdefault(i, 0)

    # compare dict values and keys for both strings
    for k,val in dict2.items():
        if k not in dict1:
            return False
        elif val > dict1[k]:
            return False
    
    return True

# Other Solutions

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

from collections import Counter

def scramble(s1, s2):
    # Python 3.10 rich comparison operators for Counter ftw!
    return Counter(s2) <= Counter(s1)