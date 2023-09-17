# Remove All Exclamation Points from a String Except at the End

"""
Remove all exclamation marks from sentence except at the end.

Examples
"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!!!"
"!Hi"     ---> "Hi"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi"

"""


# My Solution

def remove(s):
    split_point = ''
    
    # find last letter before ending exclams, split arr
    for i in range(len(s) - 1, -1, -1):
        if s[i] != '!':
            split_point = i
            break
            
    # filter out all exclams from first arr
    first_half = s[:split_point + 1].replace('!', '')
    second_half = s[split_point + 1:]
    
    # return the two combined
    return first_half + second_half

# Other Solutions

def remove(s):
    return s.replace('!', '')+ '!'*(len(s)- len(s.rstrip('!')))

import re

def remove(s):
    return re.sub(r'!+(?!!*$)', '', s)

def remove(s):
    num = 0
    for letter in s[::-1]:
        if letter != "!":
            break
        num += 1
    return s.replace("!", "") + "!" * num