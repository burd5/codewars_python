"""
Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"

"""

def remove_consecutive_duplicates(s):
    s = s.split(' ')
    result = [0]
    for word in s:
        if word != result[-1]:
            result.append(word)
    return ' '.join(result[1:])

# similar solution

def remove_consecutive_duplicates(s):
    results =[]
    for word in s.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:
            results.append(word)
    return ' '.join(results)

# solution using groupby

from itertools import groupby

def remove_consecutive_duplicates(s):
    return ' '.join(k for k,_ in groupby(s.split()))

