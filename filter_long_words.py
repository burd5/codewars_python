"""
Write a function that takes a string and an an integer n as parameters and returns a list of all words that are longer than n.

Example:

* With input "The quick brown fox jumps over the lazy dog", 4
* Return ['quick', 'brown', 'jumps']

"""

# my solution

def filter_long_words(sentence, n):
    return list(filter(lambda x: len(x) > n, sentence.split()))

# answer using list comprehension

def filter_long_words(sentence,long):
    return [word for word in sentence.split() if len(word) > long]