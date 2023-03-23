"""

You need to write a function, that returns the first non-repeated character in the given string.

If all the characters are unique, return the first character of the string.
If there is no unique character, return null in JS or Java, None in Python, '\0' in C.

You can assume, that the input string has always non-zero length.

Examples
"test"   returns "e"
"teeter" returns "r"
"trend"  returns "t" (all the characters are unique)
"aabbcc" returns null (all the characters are repeated)

"""

# my solution

def first_non_repeated(s):
    for letter in s:
        if s.count(letter) == 1:
            return letter
    return None

# solution using next() method

def first_non_repeated(s):
    return next((c for c in s if s.count(c) == 1), None)

