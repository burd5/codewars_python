# Array Leaders

"""
Definition
An element is leader if it is greater than The Sum all the elements to its right side.

Task
Given an array/list [] of integers , Find all the LEADERS in the array.

"""

# My Solution

def array_leaders(numbers):
    leaders = []
    for i,num in enumerate(numbers):
        if num > sum(numbers[i + 1:]):
            leaders.append(num)
    
    return leaders


# List Comprehension

def array_leaders(numbers):
    return [n for (i,n) in enumerate(numbers) if n>sum(numbers[(i+1):])]

