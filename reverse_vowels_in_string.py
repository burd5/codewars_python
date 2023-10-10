# Reverse Vowels in a String

"""
In this kata, your goal is to write a function which will reverse the vowels in a string. Any characters which are not vowels should remain in their original position. Here are some examples:

"Hello!" => "Holle!"
"Tomatoes" => "Temotaos"
"Reverse Vowels In A String" => "RivArsI Vewols en e Streng"
For simplicity, you can treat the letter y as a consonant, not a vowel.

Good luck!

"""

# My Long Solution

def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    
    found = []
    
    new_str = ''
    
    for i in s:
        if i in vowels:
            found.append(i)
            
    for i in s:
        if i in vowels:
            new_str += found[-1]
            found.pop(-1)
        else:
            new_str += i
            
    return new_str


# Condensed Solution

def reverse_vowels(s):
    v = [c for c in s if c.lower() in 'aeiou']
    return ''.join(v.pop(-1) if c.lower() in 'aeiou' else c for c in s)

