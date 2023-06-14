# Original Number 5kyu

"""
John has an important number, and he doesn't want others to see it.

He decided to encrypt the number, using the following steps:

His number is always a non strict increasing sequence
ie. "123"

He converted each digit into English words.
ie. "123"--> "ONETWOTHREE"

And then, rearrange the letters randomly.
ie. "ONETWOTHREE" --> "TTONWOHREEE"
John felt that his number were safe in doing so. In fact, such encryption can be easily decrypted :(

Given the encrypted string s, your task is to decrypt it, return the original number in string format.

"""

def original_number(s):
    r, s = [], list(s)
    for word, n in [('ZERO', 0), ('WTO',2), ('XSI',6), ('GEIHT',8), ('THREE',3), 
                    ('UFOR',4), ('ONE',1), ('FIVE',5), ('VSEEN',7), ('NINE',9)]: 
        while word[0] in s: 
            for c in word: s.remove(c)
            r.append(n)
    return ''.join(str(e) for e in sorted(r))

from collections import Counter 

EXECUTIONS_ORDER = [('Z', Counter("ZERO"),  '0'),
                    ('W', Counter("TWO"),   '2'),
                    ('U', Counter("FOUR"),  '4'),
                    ('X', Counter("SIX"),   '6'),
                    ('G', Counter("EIGHT"), '8'),
                    ('O', Counter("ONE"),   '1'),
                    ('H', Counter("THREE"), '3'),
                    ('F', Counter("FIVE"),  '5'),
                    ('V', Counter("SEVEN"), '7'),
                    ('I', Counter("NINE"),  '9')]

def original_number(s):
    ans, count, executions = [], Counter(s), iter(EXECUTIONS_ORDER)
    while count:
        c, wordCount, value = next(executions)
        ans.extend([value]*count[c])
        for _ in range(count[c]): count -= wordCount
    return ''.join(sorted(ans))