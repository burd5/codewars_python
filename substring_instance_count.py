"""
Complete the solution so that it returns the number of times the search_text is 
found within the full_text.

Usage example:

solution('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
solution('aaabbbcccc', 'bbb') # should return 1

"""

# my solution

def solution(full_text, search_text):
    stripped_str = full_text.replace(search_text, '')
    return len(full_text) + 1 if search_text == '' else (len(full_text) - len(stripped_str))/len(search_text)

# simple solution

def solution(full_text, search_text):
    return full_text.count(search_text)

