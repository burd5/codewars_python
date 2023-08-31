# Substring Fun

"""
Complete the function that takes an array of words.

You must concatenate the nth letter from each word to construct a new word which should be returned as a string, where n is the position of the word in the list.

For example:

["yoda", "best", "has"]  -->  "yes"
  ^        ^        ^
  n=0     n=1     n=2

"""

# My Solution

def nth_char(words):
	return ''.join([words[i][i] for i in range(len(words))])

# Other Solutions

def nth_char(words):
	return ''.join(w[i] for i,w in enumerate(words))

def nth_char(words):
    result = ""

    for index, word in enumerate(words):
        result += word[index]

    return result