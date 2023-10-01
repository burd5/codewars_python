# Alphabetically Ordered

"""
Your task is very simple. Just write a function that takes an input string of lowercase letters and returns true/false depending on whether the string is in alphabetical order or not.

Examples (input -> output)
"kata" -> false ('a' comes after 'k')
"ant" -> true (all characters are in alphabetical order)

"""

# My Solution

def alphabetic(s):
    for i in range(1, len(s)):
        if s[i] < s[i - 1]: return False
    return True

# Other Solutions

def alphabetic(s):
    return sorted(s) == list(s)

def alphabetic(s):
    return all(a<=b for a,b in zip(s, s[1:]))