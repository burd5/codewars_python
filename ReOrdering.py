"""
There is a sentence which has a mistake in its ordering.

The part with a capital letter should be the first word.

Please build a function for re-ordering

Examples
>>> re_ordering('ming Yao')
'Yao ming'

>>> re_ordering('Mano donowana')
'Mano donowana'

>>> re_ordering('wario LoBan hello')
'LoBan wario hello'

>>> re_ordering('bull color pig Patrick')
'Patrick bull color pig'

"""

# my solution

def re_ordering(text):
    arr = text.split(' ')
    for word in arr:
        if word[0].isupper():
            arr.remove(word)
            arr.insert(0, word)
    return ' '.join(arr)

# other solutions

def re_ordering(name):
    return ' '.join(sorted(name.split(), key=str.islower))