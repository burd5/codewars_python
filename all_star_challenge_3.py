"""
Create a function, called removeVowels (or remove_vowels), that takes a string 
argument and returns that same string with all vowels removed (vowels are "a", 
"e", "i", "o", "u").

removeVowels("drake") // => "drk"
removeVowels("aeiou") // => ""

"""

# my solution

def remove_vowels(strng):
    vowels = 'aeiou'
    for letter in strng:
        if letter in vowels:
            strng = strng.replace(letter, '')
            
    return strng

# list comprehension answer

def remove_vowels(strng):
    return ''.join([i for i in strng if i not in 'aeiou'])