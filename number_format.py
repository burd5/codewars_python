# Number Format - Codewars 6kyu

"""
Format any integer provided into a string with "," (commas) in the correct places.

Example:

For n = 100000 the function should return '100,000';
For n = 5678545 the function should return '5,678,545';
for n = -420902 the function should return '-420,902'.

"""

# my solution

def number_format(n):
    comma = list(str(n))
    negative = False
    if comma[0] == '-':
        comma.remove('-')
        negative = True
    indexes = []
    length = len(comma)
    while length > 3:
        indexes.append(length - 3)
        length -= 3
    for index in indexes:
        comma.insert(index, ',')
    return '-' + ''.join(comma) if negative == True else ''.join(comma)

# using 

def number_format(n):
    return f'{n:,}'

def number_format(n):
    return format(n, ',')