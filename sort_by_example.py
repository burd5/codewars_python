"""
Given an Array and an Example-Array to sort to, write a function that sorts the Array following the Example-Array.

Assume Example Array catalogs all elements possibly seen in the input Array. However, the input Array does not necessarily have to have all elements seen in the Example.

Example:

Arr: [1,3,4,4,4,4,5]

Example Arr: [4,1,2,3,5]

Result: [4,4,4,4,1,3,5]

"""

# my solution

def example_sort(arr, example_arr):
    return sorted(arr, key=lambda v: example_arr.index(v))

# less code solution

def example_sort(arr, example_arr):
    return sorted(arr, key=example_arr.index)