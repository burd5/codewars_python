# Proof Read

"""
You've just finished writing the last chapter for your novel when a virus suddenly infects your document. It has swapped the 'i's and 'e's in 'ei' words and capitalised random letters. Write a function which will:

a) remove the spelling errors in 'ei' words. (Example of 'ei' words: their, caffeine, deceive, weight)

b) only capitalise the first letter of each sentence. Make sure the rest of the sentence is in lower case.

Example: He haD iEght ShOTs of CAffIEne. --> He had eight shots of caffeine.

"""


# My Solution

def proofread(string):
    switch = string.lower().replace('ie', 'ei')
    return '. '.join(map(lambda s: s.strip().capitalize(), switch.split('.'))).rstrip(' ')

# Simpler Solution

def proofread(s):    
    return '. '.join(i.lower().replace('ie', 'ei').capitalize() for i in s.split('. '))

