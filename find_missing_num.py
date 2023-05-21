"""
The following was a question that I received during a technical interview for an entry level software developer position. I thought I'd post it here so that everyone could give it a go:

You are given an unsorted array containing all the integers from 0 to 100 inclusively. However, one number is missing. Write a function to find and return this number. What are the time and space complexities of your solution?

"""

# my solution

def missing_no(nums):
    sum_100 = sum(range(1,101))
    return sum_100 - sum(nums)

# for loop solution

def missing_no(nums):
    for i in range(0, 101):
        if not i in nums: return i