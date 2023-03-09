"""
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.

"""


def swap(st):
    vowels = 'aeiou'
    new_string = ''
    for letter in st:
        if letter in vowels:
            new_string += letter.upper()
        else:
            new_string += letter
            
    return new_string

# looked at solution using maketrans()

def swap(st):
  tr = str.maketrans('aeiou', 'AEIOU')
  return st.translate(tr);