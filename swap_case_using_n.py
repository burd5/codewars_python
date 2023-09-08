# Swap Case Using N

"""
Your job is to change the given string s using a non-negative integer n.

Each bit in n will specify whether or not to swap the case for each alphabetic character in s: if the bit is 1, swap the case; if its 0, leave it as is. When you finish with the last bit of n, start again with the first bit.

You should skip the checking of bits when a non-alphabetic character is encountered, but they should be preserved in their original positions.

Examples
swap("Hello world!", 11)  -->  "heLLO wORLd!"
...because 11 is 1011 in binary, so the 1st, 3rd, 4th, 5th, 7th, 8th and 9th alphabetical characters have to be swapped:

H e l l o   w o r l d !
1 0 1 1 1 x 0 1 1 1 0 x
^   ^ ^ ^    ^ ^ ^

"""

# My Solution

def swap(s,n):
    # get binary of n, multiply by length of s
    binary_n = format(n, 'b')
    count = 0
 
    # new string to hold converted value
    swapped = ''
    
    # loop through string, if isalpha(), switch upper/lower, skip spaces and special characters
    for i in range(len(s)):
        if s[i].isalpha():
            if binary_n[count] == '1':
                swapped += switch_case(s[i])
            else:
                swapped += s[i]
            if count == len(binary_n) - 1:
                count = 0
            else:
                count += 1
        else:
            swapped += s[i]
            
    return swapped
            
def switch_case(s):
    if s.upper() == s:
        return s.lower()
    else:
        return s.upper()
    

# Other Solutions

from itertools import cycle

def swap(s,n):
    b = cycle(bin(n)[2:])
    return "".join(c.swapcase() if c.isalpha() and next(b) == '1' else c for c in s)

def swap(s,n):
    n = str(bin(n))[2:]
    index = 0
    new_s = ''
    for letter in s:
        if letter.isalpha():
            if n[index%len(n)]=='1':
                new_s += letter.swapcase()
            else:
                new_s += letter
            index+=1
        else:
            new_s += letter
    return new_s
