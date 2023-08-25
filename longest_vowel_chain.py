# Longest Vowel Chain

"""
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

"""

# My Solution

def solve(s):
    counter = 0
    longest = 0
    vowels = 'aeiou'
    for i in s:
        if i in vowels:
            counter += 1
            if counter > longest:
                longest = counter
        else:
            counter = 0
    return longest

# Other Solutions

import re

def solve(s):
    return max(len(x.group(0)) for x in re.finditer(r'[aeiou]+', s))


def solve(s):
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))