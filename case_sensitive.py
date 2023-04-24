"""
Your task is very simple. Given an input string s, case_sensitive(s), check 
whether all letters are lowercase or not. Return True/False and a list of all 
the entries that are not lowercase in order of their appearance in s.

For example, case_sensitive('codewars') returns [True, []], but 
case_sensitive('codeWaRs') returns [False, ['W', 'R']].

"""

# my solution

def case_sensitive(s):
    uppers = []
    for letter in s:
        if letter == letter.upper():
            uppers.append(letter)
    return [False, uppers] if len(uppers) > 0 else [True, uppers]

# better solution

def case_sensitive(s):
    return [s.islower() or not s, [c for c in s if c.isupper()]]