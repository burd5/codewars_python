"""
Task
Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Notes
Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.

Example
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1

"""

# my solution

def least_larger(a, i): 
    compare_num = a[i]
    answer = float('inf')
    for num in a:
        if num > compare_num and num < answer:
            answer = num
            
    if answer == float('inf'): return -1
    else: return a.index(answer)

# other solution

def least_larger(a, i):
    b = [x for x in a if x>a[i]]
    return a.index(min(b)) if b else -1