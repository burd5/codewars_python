"""
Your task is to create a function that given a sequence and a predicate, returns 
True if only some (but not all) the elements in the sequence are True after 
applying the predicate

Examples
some('abcdefg&%$', str.isalpha)
>>> True

some('&%$=', str.isalpha)
>>> False

some('abcdefg', str.isalpha)
>>> False

some([4, 1], lambda x: x>3)
>>> True

some([1, 1], lambda x: x>3)
>>> False

some([4, 4], lambda x: x>3)
>>> False
"""

# my solution

def some_but_not_all(seq, pred):
    output = list(map(pred, list(seq)))
    return any(output) and not all(output)

# simplified answer

def some_but_not_all(seq, pred): 
    return any(map(pred, seq)) and not all(map(pred, seq))