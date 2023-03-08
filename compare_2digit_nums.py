"""
You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.

Example:

compare(13,14)=50%;
compare(23,22)=50%;
compare(15,51)=100%;
compare(12,34)=0%.

"""

def compare(a, b):
    a = str(a)
    b = str(b)
    
    if a == b or a[::-1] == b:
        return '100%'
    
    if a[0] in b or a[1] in b:
        return '50%'
    
    return '0%'


# another way to write it

def compare(a, b):
    fir = sorted(str(a))
    sec = sorted(str(b))
    return '100%' if fir == sec else '50%' if fir[0] in sec or fir[1] in sec else '0%'