"""
In this exercise, you will create a function that takes an integer, i. With it you must do the following:

Find all of its multiples up to and including 100,

Then take the digit sum of each multiple (eg. 45 -> 4 + 5 = 9),

And finally, get the total sum of each new digit sum.

Note: If the digit sum of a number is more than 9 (eg. 99 -> 9 + 9 = 18) then you do NOT have to break it down further until it reaches one digit.

Example (if i is 25):

Multiples of 25 up to 100 --> [25, 50, 75, 100]

Digit sum of each multiple --> [7, 5, 12, 1]

Sum of each new digit sum --> 25

"""

# my solution

import math
def procedure(num):
    # variable to keep track of sum of digits
    mult_sum = 0
    # for loop to add multiples less than or equal to 100
    # if digit len > 1, split and sum, otherwise just add to sum
    for i in range(1, math.ceil(101/num)):
        current_num = num * i
        mult_sum += sum([int(x) for x in str(current_num)])
        
    # return sum
    return mult_sum

# one line solution

def procedure(n):
    return sum(int(d) for i in range(n, 101, n) for d in str(i))