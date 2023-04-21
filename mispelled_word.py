"""
Create a function mispelled(word1, word2):

mispelled('versed', 'xersed') # returns True
mispelled('versed', 'applb') # returns False
mispelled('versed', 'v5rsed') # returns True
mispelled('1versed', 'versed') # returns True
mispelled('versed', 'versed') #returns True 
It checks if the word2 differs from word1 by at most one character.

This can include an extra char at the end or the beginning of either of words.

In the tests that expect true, the mispelled word will always differ mostly by one character. If the two words are the same, return True.

"""

# my solution
def mispelled(word1,word2):
    if len(word1) == len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        return count <= 1
    if len(word1) > len(word2):
        if word1[1:] == word2 or word1[:-1] == word2: return True
        else: return False
    if len(word2) > len(word1):
        if word2[1:] == word1 or word2[:-1] == word1: return True
        else: return False

# other clever solution

def mispelled(word1, word2):
    l1, l2 = len(word1), len(word2)
    if l1 == l2:
        return sum(1 for a, b in zip(word1, word2) if a != b) <= 1
    if l1 - l2 == 1:
        return word1.startswith(word2) or word1.endswith(word2)
    if l1 - l2 == -1:
        return word2.startswith(word1) or word2.endswith(word1)
    return False