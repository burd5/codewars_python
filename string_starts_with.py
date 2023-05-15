"""
Challenge: Given two null-terminated strings in the arguments "string" and "prefix", determine if "string" starts with the "prefix" string. Return true or false.

Example:

startsWith("hello world!", "hello"); // should return true
startsWith("hello world!", "HELLO"); // should return false
startsWith("nowai", "nowaisir"); // should return false
Addendum: For this problem, an empty "prefix" string should always return true for any value of "string".

If the length of the "prefix" string is greater than the length of the "string", return false.

The check should be case-sensitive, i.e. startsWith("hello", "HE") should return false, whereas startsWith("hello", "he") should return true.

"""

# my solution

def starts_with(st, prefix): 
    if len(prefix) > len(st): return False
    return prefix == st[:len(prefix)]

# other solution

def starts_with(st, prefix): 
    return st.startswith(prefix)