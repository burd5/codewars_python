"""
Everybody knows a little german, right? But remembering the correct articles is 
a tough job. Write yourself a little helper, that returns the noun with the 
matching article:

each noun containing less than 2 vowels has the article "das"
each noun containing 2/3 vowels has the article "die"
each noun containing more than 3 vowels has the article "der"
Caution: Vowels are "a,e,i,o,u". Umlaute (ä ö ü) are also being counted!

"""

# my solution

def der_die_das(wort):
    vowels = 'aeiouäöü'
    counter = 0
    for letter in wort:
        if letter.lower() in vowels: counter += 1
    
    if counter < 2: return f'das {wort}'
    elif counter <= 3: return f'die {wort}'
    elif counter > 3: return f'der {wort}'

# cleaner solution

def der_die_das(wort):
    a = sum(x in "aAeEiIoOuUäöü" for x in wort)
    return f'{"das" if a < 2 else "die" if a < 4 else "der"} {wort}'