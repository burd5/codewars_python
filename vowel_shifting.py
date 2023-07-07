# Vowel Shifting - Codewars 6kyu

"""
You get a "text" and have to shift the vowels by "n" positions to the right.
(Negative value for n should shift to the left.)
"Position" means the vowel's position if taken as one item in a list of all vowels within the string.
A shift by 1 would mean, that every vowel shifts to the place of the next vowel.

Shifting over the edges of the text should continue at the other edge.

Example:

text = "This is a test!"
n = 1
output = "Thes is i tast!"

text = "This is a test!"
n = 3
output = "This as e tist!"

If text is null or empty return exactly this value.
Vowels are "a,e,i,o,u".

"""
# My Solution

def vowel_shift(text,n):
    if n == 0: return text
    vowels = 'aeiouAEIOU'
    found = [x for x in text if x in vowels]
    if n > 0:
        for i in range(n):
            found = found[-1:] + found[: -1]
    elif n < 0:
        for i in range(n,0,1):
            found = found[1:] + found[:1]
    for i in range(len(text)):
        if text[i] in vowels:
            text = text[:i] + found[0] + text[i + 1:]
            found.pop(0)
    return text