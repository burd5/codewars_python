# Dictionary of Factors

"""
The objective of this Kata is to write a function that creates a dictionary of factors for a range of numbers.

The key for each list in the dictionary should be the number. The list associated with each key should possess the factors for the number.

If a number possesses no factors (only 1 and the number itself), the list for the key should be ['None']

The function possesses two arguments (n and m). Where n is the starting number and m is the ending number.

For example: All factors for 2 (n) through to 6 (m) with the number being the key in the dictionary:

{2: ['None'], 3: ['None'], 4: [2], 5: ['None'], 6: [2, 3]}

"""

# My Solution

def factorsRange(n, m):
    dict = {}
    for i in range(n, m + 1):
        factors = []
        for j in range(1, i):
            if i % j == 0 and j != 1:
                factors.append(j)
        if factors:
            dict[i] = factors
        else:
            dict[i] = ['None']    
    return dict

# One Liner

def factorsRange(n, m):
    return {i: [j for j in range(2, i) if i % j == 0] or ['None'] for i in range(n, m + 1)}
