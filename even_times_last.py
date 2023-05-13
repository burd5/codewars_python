"""
Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.

Indices in sequence start from 0.

If the sequence is empty, you should return 0.

"""

# my solution

def even_last(numbers): 
    return 0 if numbers == [] else sum([x for i,x in enumerate(numbers) if i % 2 == 0]) * numbers[-1]

