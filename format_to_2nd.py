"""
Given some positive integers, I wish to print the integers such that all take up the same width by adding a minimum number of leading zeroes. No leading zeroes shall be added to the largest integer.

For example, given 1, 23, 2, 17, 102, I wish to print out these numbers as follows:

001
023
002
017
102

"""

# my solution

def print_nums(*list):
    if list == (): return ''
    string = ''
    maximum = len(str(max(list)))
    for num in list:
        if num == list[-1]:
            string += str(num).rjust(maximum, '0')
        else:
            string += str(num).rjust(maximum, '0') + '\n'
            
    return string

# other solution using zfill

def print_nums(*arr):
    if not arr: return ''
    ln = len(str(max(arr)))
    return '\n'.join(str(c).zfill(ln) for c in arr)

