# Minimize Sum of Array

"""

Task
Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .

Notes
Array/list will contain positives only .
Array/list will always have even size
Input >> Output Examples
minSum({5,4,2,3}) ==> return (22) 
Explanation:
The minimum sum obtained from summing each two integers product ,  5*2 + 3*4 = 22

"""

# My Solution

# Sort array and multiply last and first item together. Add the products of these pairs to a variable and continue through the array
def min_sum(arr):
    # Sort array
    arr = sorted(arr)
    
    # Use pointers to move through array from both sides
    l,r = 0, len(arr) - 1
    
    # Add product of two integers to this variable to keep track of the count
    final_sum = 0
    
    # While l is less than r (i.e. Haven't met in the middle), continue to move in from both sides
    while l < r:
        final_sum += arr[l] * arr[r]
        l += 1
        r -= 1

# Condensed Answers

def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))


def min_sum(arr):
    arr.sort()
    return sum(i * arr.pop() for i in arr)