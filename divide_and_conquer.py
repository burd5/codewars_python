"""
Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number.

"""

# MY SOLUTION

def div_con(x):
    strings = [int(num) for num in x if isinstance(num, str)]
    integers = [num for num in x if isinstance(num, int)]
    return sum(integers) - sum(strings)

# MORE CONCISE WAY TO WRITE IT

def div_con(x):
    return sum([a for a in x if isinstance(a, int)]) - sum([int(a) for a in x if not isinstance(a, int)])