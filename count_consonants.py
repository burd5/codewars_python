"""

Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u.


"""


def consonant_count(s):
    consonants = 'aeiouAEIOU1234567890!@#$%^&* _+'
    
    final_string = [x for x in s if x not in consonants]
    
    return len(final_string)

# other solution

def consonant_count(s):
    vowels = 'aeiou'
    counter = 0
    for letter in s.lower():
        if (letter not in vowels) and letter.isalpha():
            counter += 1
    return counter

# other solution

def consonant_count(str):
    return sum(1 for c in str if c.isalpha() and c.lower() not in "aeiou")