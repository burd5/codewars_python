"""
Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.

"""

# my solution

def sum_no_duplicates(l):
    # set dict to receive counts of values
    dict = {}
    # loop through original list, if key exists already - add one, else - add key to dict with a value of one
    for num in l:
        if num in dict:
            dict[num] += 1
        else: 
            dict[num] = 1
    # set sum counter
    sum = 0
    # loop through dict, adding key to sum if the value is equal to one
    for key,value in dict.items():
        if value == 1:
            sum += key
   
    return sum

# simple solution using Counter

from collections import Counter

def sum_no_duplicates(nums):
    return sum(k for k, v in Counter(nums).items() if v == 1)


# another solution

def sum_no_duplicates(l):
    new = []
    for x in l:
        if l.count(x) == 1:
            new.append(x)
    return sum(new)