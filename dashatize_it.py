# Dashatize It

"""
Given a variable n,

If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

If n is not an integer, return the string "None".

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'

"""
# My Solution

def dashatize(n):
    if not isinstance(n, int): return 'None'
    n = str(n).lstrip('-')
    final_str = ''
    for i in range(len(n)):
        curr = int(n[i]) % 2
        if curr:
            final_str += '-' + n[i] + '-'
        else:
            final_str += n[i]
            
    return final_str.replace('--', '-').strip('-')

# Condensed Version

def dashatize(num):
    try:
        return ''.join(['-'+i+'-' if int(i)%2 else i for i in str(abs(num))]).replace('--','-').strip('-')
    except:
        return 'None'