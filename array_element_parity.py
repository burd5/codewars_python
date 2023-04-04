"""
In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.

Examples:

[1, -1, 2, -2, 3] => 3

3 has no matching negative appearance

[-3, 1, 2, 3, -1, -4, -2] => -4

-4 has no matching positive appearance

[1, -1, 2, -2, 3, 3] => 3

(the only-positive or only-negative integer may appear more than once)

Good luck!

"""

# my solution

def solve(arr):
    dict = {}
    for num in arr:
        if -num in dict:
            dict[num * -1] -= 1
        else: dict[num] = 1
    
    answer = [val for val, key in dict.items() if key != 0]
    return answer[0]

# other, simpler solutions

def solve(arr): return sum(set(arr))

def solve(arr):
    for a in arr:
        if -a not in arr:
            return a

