"""

Your job is to figure out the index of which vowel is missing from a given string:

A has an index of 0,
E has an index of 1,
I has an index of 2,
O has an index of 3,
U has an index of 4.
Notes: There is no need for string validation and every sentence given will contain all vowels but one. Also, you won't need to worry about capitals.

Examples
"John Doe hs seven red pples under his bsket"          =>  0  ; missing: "a"
"Bb Smith sent us six neatly arranged range bicycles"  =>  3  ; missing: "o"

"""

# my solution

import re
def absent_vowel(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # vowels arr
    vowels_filter = list(set(re.findall(r'[aeiou]', x)))
    
    index = ''.join([x for x in vowels if x not in vowels_filter])
    
    return vowels.index(index)

# other solutions

def absent_vowel(x): 
    strings = ['a','e','i','o','u']
    for i in strings:
        if i not in x:
          return strings.index(i)
        

def absent_vowel(x): 
    return 'aeiou'.index((set('aeiou') - set(x.lower())).pop())

def absent_vowel(x): 
    return ['aeiou'.index(i) for i in 'aeiou' if i not in x][0]