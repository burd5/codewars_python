"""
Create a function named rotate() that accepts a string argument and returns an array of strings with each letter from the input string being rotated to the end.

rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]
"""

# my solution using string splicing

def rotate(str_):
    rotated_str = []
    for i in range(len(str_)):
        rotated_str.append(str_[i + 1:] + str_[:i + 1])
    
    return rotated_str

# one liner using list comprehension

def rotate(str_):
    return [str_[i + 1:] + str_[:i + 1] for i in range(len(str_))]