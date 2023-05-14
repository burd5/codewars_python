"""
Create a function that takes index [0, 8] and a character. It returns a string with columns. Put character in column marked with index.

Ex.: index = 2, character = 'B'

| | |B| | | | | | |
 0 1 2 3 4 5 6 7 8
Assume that argument index is integer [0, 8]. Assume that argument character is 
string with one character.

"""

# my solution

def build_row_text(index, character):
    return ''.join(['| ' if x != index else f'|{character}' for x in range(9)] + ['|'])

# other "pre-build" solutions

def build_row_text(index, character):
    a=list('|||||||||')
    a[index]="|"+character+"|"
    return " ".join(a)

def build_row_text(index, character):
    columns = [' '] * 9
    columns[index] = character
    return ('|' + '|'.join(columns) + '|')