"""
Implement a function find_matched_by_pattern(pattern) that returns a predicate function, testing a string input and returning true if the string is matching the pattern, false otherwise.

A word is considered a match for a given pattern if the first occurrence of each letter of the pattern is found in the same order in the word. If a character in the pattern is duplicated, the same logic applies further.

The pattern will always be a string of size 3.

Example of use:

predicate = find_matched_by_pattern('acs')
predicate('access') # True
predicate('sacrifice') # False 

"""

