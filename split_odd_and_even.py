"""
Complete function splitOddAndEven, accept a number n(n>0), return an array that
contains the continuous parts of odd or even digits.

Please don't worry about digit 0, it won't appear ;-)

Examples
splitOddAndEven(123)  ===  [1,2,3]

splitOddAndEven(223)  ===  [22,3]

splitOddAndEven(111)  ===  [111]

splitOddAndEven(13579)  ===  [13579]

splitOddAndEven(135246)  ===  [135,246]

splitOddAndEven(123456)  ===  [1,2,3,4,5,6]

"""

# solutions using groupby and regex

from itertools import groupby

def split_odd_and_even(n):
    return [int("".join(g))
        for i, g in groupby(str(n), key=lambda x: int(x) % 2)]

def split_odd_and_even(n):
    
    import re
  
    return [int(i) for i in re.findall(r"[2468]+|[13579]+", str(n))]