"""

Task
Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

"""

# my solution
def product_array(numbers):
    product_arr = []
    for i in range(len(numbers)):
        total = 1
        for idx, num in enumerate(numbers):
            if i != idx: total *= num
        product_arr.append(total)
        
    return product_arr

# solutions using imported packages

from operator import mul
from functools import reduce

def product_array(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]

# other solution

from numpy import prod

def product_array(numbers):
    p = prod(numbers)
    return [p // i for i in numbers]
