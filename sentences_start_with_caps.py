# Sentences should start with capital letters

"""
In English, all words at the begining of a sentence should begin with a capital letter.

You will be given a paragraph that does not use capital letters. Your job is to capitalise the first letter of the first word of each sentence.

For example,

input:

"hello. my name is inigo montoya. you killed my father. prepare to die."

output:

"Hello. My name is inigo montoya. You killed my father. Prepare to die."

"""

# My Solution

def fix(paragraph):
    par_arr = paragraph.split('. ')
    par_arr = [x.capitalize() for x in par_arr]
    return '. '.join(par_arr)

# One Line Solution

def fix(paragraph):
    return '. '.join(s.capitalize() for s in paragraph.split('. '))