"""
Write a function that will randomly upper and lower characters in a string - 
randomCase() (random_case() for Python).

A few examples:

randomCase("Lorem ipsum dolor sit amet, consectetur adipiscing elit") == "lOReM 
ipSum DOloR SiT AmeT, cOnsEcTEtuR aDiPiSciNG eLIt"

randomCase("Donec eleifend cursus lobortis") == "DONeC ElEifEnD CuRsuS LoBoRTIs"

"""

# my solution

import random

def random_case(x):
    new_str = ''
    for letter in x:
        int = random.randint(0,1)
        if int == 0:
            new_str += letter.upper()
        else: new_str += letter.lower()
    return new_str

# one liner

import random

def random_case(x):
    return "".join([random.choice([c.lower(), c.upper()]) for c in x])