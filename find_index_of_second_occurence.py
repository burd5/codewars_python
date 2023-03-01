"""

In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in the string. If there is no such letter in the string, then the function should return -1. If the letter occurs only once in the string, then -1 should also be returned.

Examples:

second_symbol('Hello world!!!','l') --> 3
second_symbol('Hello world!!!', 'A') --> -1

"""


def second_symbol(s, symbol):
    
    return s.find(symbol, s.find(symbol)+ 1)


# similar idea with indexes

def second_symbol(s, c):
    if not c or s.count(c) < 2:
        return -1
    return s.index(c, s.index(c) + 1)