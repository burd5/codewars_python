"""
Given a string as input, move all of its vowels to the end of the string, in the same order as they were before.

Vowels are (in this kata): a, e, i, o, u

Note: all provided input strings are lowercase.

Examples
"day"    ==>  "dya"
"apple"  ==>  "pplae"

"""

# my solution
def move_vowels(input):
    vowels = 'aeiou'
    input = list(input)
    end_chars = []
    for i,letter in enumerate(input):
        if letter in vowels:
            end_chars.append(letter)
    input = [x for x in input if x not in vowels]
    return ''.join(input + end_chars)

# other solution using sorted

def move_vowels(s): 
    return ''.join(sorted(s, key=lambda k: k in 'aeiou'))