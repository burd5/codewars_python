# Convert Pascal Case into String Case

"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"

"""

# My Solution

def to_underscore(string):
    if isinstance(string, int): return str(string)
    new_string = ''
     # loop through string and replace uppercase string with'_(lowercase letter)'
    for i,x in enumerate(string):
        if x.isnumeric(): new_string += str(x)
        elif i == 0:
            new_string += x.lower()
        elif x == x.upper():
            new_string += f'_{x.lower()}'
        else:
            new_string += x
            
# Other Solutions

import re

def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()    

"""
The regex picks any character followed by an uppercase letter and sets two groups

\1 = [any character]

\2 = [the uppercase letter that follows]

Then it replaces this pattern by the format "\1_\2"

So, for the string 'CodeWarsPascalCase' it will pick 'eW', 'rP' and 'lC' and replace with the new given pattern ('e_W', 'r_P' and 'l_C')

"""

def to_underscore(string):
    string = str(string)
    camel_case = string[0].lower()
    for c in string[1:]:
        camel_case += '_{}'.format(c.lower()) if c.isupper() else c
    return camel_case

def to_underscore(string):
    return ''.join('_'+c.lower() if c.isupper() else c for c in str(string)).lstrip('_')