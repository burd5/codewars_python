"""
Bob is a lazy man.

He needs you to create a method that can determine how many letters 
(both uppercase and lowercase ASCII letters) and digits are in a given string.

Example:

"hel2!lo" --> 6

"wicked .. !" --> 6

"!?..A" --> 1

"""

# my solution

def count_letters_and_digits(s):
    return len([x for x in s if x.isnumeric() or x.isalpha()])


# other solution using isalnum() and map()

def count_letters_and_digits(s):
    return sum(map(str.isalnum, s))