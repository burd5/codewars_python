# Maximum and Minimum Difference

"""
Given two array of integers(arr1,arr2). Your task is going to find a pair of numbers(an element in arr1, and another element in arr2), their difference is as big as possible(absolute value); Again, you should to find a pair of numbers, their difference is as small as possible. Return the maximum and minimum difference values by an array: [  max difference,  min difference  ]

For example:

Given arr1 = [3,10,5], arr2 = [20,7,15,8]
should return [17,2] because 20 - 3 = 17, 10 - 8 = 2

"""
# My Solution (Slow)

def max_and_min(arr1,arr2):
    maximum = max(max(arr1) - min(arr2), max(arr2) - min(arr1))
    minimum = float('inf')
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            diff = abs(arr1[i] - arr2[j])
            if diff < minimum: minimum = diff
            
    return [maximum, minimum]

# Other Solution

def max_and_min(arr1,arr2):
    diffs = [abs(x-y) for x in arr1 for y in arr2]
    return [max(diffs), min(diffs)]