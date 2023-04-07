"""


"""

# my solution

import re
from collections import OrderedDict

def lottery(s):
    ints = re.findall(r'[0-9]', s)
    answer = []
    if len(ints) >= 1:
        for num in ints:
            if num not in answer:
                answer.append(num)
        return ''.join(answer)
    else:
        return "One more run!"
    
# other solutions

def lottery(s):
    return "".join(dict.fromkeys(filter(str.isdigit, s))) or "One more run!"

def lottery(s):
    
    result = ''
    
    for i in s:
        if i.isdigit() and i not in result:
            result += i
    
    return result or 'One more run!'
