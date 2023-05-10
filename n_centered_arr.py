"""
An array is called centered-N if some consecutive sequence of elements of the array sum to N and this sequence is preceded and followed by the same number of elements.

Example:

[3,2,10,4,1,6,9] is centered-15
because the sequence 10,4,1 sums to 15 and the sequence 
is preceded by two elements [3,2] and followed by two elements [6,9]
Write a method called isCenteredN that returns :

true if its array argument is not empty and centered-N or empty and centered-0
otherwise returns false.

"""

# other solution

def is_centered(arr: list, n: int) -> bool:
    i, j = 0, len(arr) - 1
    s = sum(arr)
    while i < j and s != n:
        s -= arr[i]
        s -= arr[j]
        i += 1
        j -= 1
    return s == n

