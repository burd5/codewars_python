"""
Description:
Give you a sentence s. It contains some words and separated by spaces. Another arguments is n, its a number(1,2 or 3). You should convert s to camelCase n.

There are three kinds of camelCase:

camelCase 1: The first letter of each word should be capitalized. 
              Except for the first word.

Example: "Hello world"  -->  "helloWorld"

camelCase 2: The last letter of each word should be capitalized. 
              Except for the last word. 

Example: "Hello world"  -->  "hellOworld"

camelCase 3: The first and last letters of each word should be capitalized. 
              Except for the first and lasts letter of sentence. 

Example: "Hello world"  -->  "hellOWorld" 

"""

# my solution

def toCamelCase(s,n):
    if n == 1:
        return camelCaseOne(s)
    elif n == 2:
        return camelCaseTwo(s)
    else:
        return camelCaseThree(s)
    
def camelCaseOne(s):
    s = s.split(' ')
    camel_case = ''
    for i, word in enumerate(s):
        if i == 0:
            camel_case += word.lower()
        else:
            camel_case += word.title()
    return camel_case

def camelCaseTwo(s):
    s = s.split(' ')
    camel_case = ''
    for i, word in enumerate(s):
        if i != len(s) - 1:
            camel_case += word[:-1].lower() + word[-1].upper()
        else:
            camel_case += word.lower()
    return camel_case

def camelCaseThree(s):
    s = s.split(' ')
    camel_case = ''
    for i, word in enumerate(s):
        if i == len(s) - 1:
            camel_case += word[0].upper() + word[1:].lower()
        elif i == 0:
            camel_case += word[:-1].lower() + word[-1].upper()
        else:
            camel_case += word[0].upper() + word[1:-1].lower() + word[-1].upper()
    return camel_case

# other solution


def toCamelCase(s, n):
    if n == 1:
        return s[0].lower() + s.title().replace(' ', '')[1:]
    elif n == 2:
        return ''.join(map(lambda x: x[:-1].lower() + x[-1].upper(), s.split()))[:-1] + s[-1].lower()
    else:
        return ''.join(map(lambda x: x[:-1] + x[-1].upper(), (s[0].lower() + s.title()[1:]).split()))[:-1] + s[-1].lower()