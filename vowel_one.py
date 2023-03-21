"""

Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.

Examples:

vowelOne "abceios" -- "1001110"

vowelOne "aeiou, abc" -- "1111100100"

"""

# my solution

def vowel_one(s):
    vowels = 'aeiou'
    binary_str = ''
    for letter in s:
        if letter.lower() in vowels:
            binary_str += '1'
        else:
            binary_str += '0'
            
    return binary_str

# efficient way to write it

def vowel_one(s):
    return "".join("1" if c in "aeiou" else "0" for c in s.lower())

