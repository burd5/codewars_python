"""
You should write a function that takes a string and a positive integer n, splits the string into parts of length n and returns them in an array. It is ok for the last element to have less than n characters.

If n is not a number or not a valid size (> 0) (or is absent), you should return an empty array.

If n is greater than the length of the string, you should return an array with the only element being the same string.

Examples:

string_chunk('codewars', 2) # ['co', 'de', 'wa', 'rs']
string_chunk('thiskataeasy', 4) # ['this', 'kata', 'easy']
string_chunk('hello world', 3) # ['hel', 'lo ', 'wor', 'ld']
string_chunk('sunny day', 0) # []

"""

# my solution

def string_chunk(st,n = 0):
    if n == 0 or str(n) == n: return []
    arr = [st[i: i + n] for i in range(0, len(st), n)]
    return arr

# other solution

def string_chunk(string, n=0):
    return [string[i:i+n] for i in range(0,len(string), n)] if isinstance(n, int) and n > 0 else []