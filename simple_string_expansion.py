# Simple String Expansion

"""
Consider the following expansion:

solve("3(ab)") = "ababab"     -- because "ab" repeats 3 times
solve("2(a3(b))") = "abbbabbb" -- because "a3(b)" == "abbb", which repeats twice.
Given a string, return the expansion of that string.

Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis. There will be no letters or numbers after the last closing parenthesis.

"""
# My Solution

def solve(st):
    # variable to hold current string
    curr = ''
    
    # loop through each letter of the string
    # identify letters and numbers
    # multiply current string by int when relevant
    for s in reversed(st):
        if s.isalpha():
            curr = s + curr
        if s.isnumeric():
            curr = curr * int(s)
    return curr

# Other Solutions

def solve(s):
    s1 = s[::-1]
    s2 = ''
    for i in s1:
        if i.isalpha():
            s2 += i
        elif i.isdigit():
            s2 = s2*int(i)
    return s2[::-1]
