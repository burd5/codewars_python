# Concatenated Sum 

"""
The number 198 has the property that 198 = 11 + 99 + 88, i.e., if each of its digits is concatenated twice and then summed, the result will be the original number. It turns out that 198 is the only number with this property. However, the property can be generalized so that each digit is concatenated n times and then summed.

Examples
original number =2997 , n=3
2997 = 222+999+999+777 and here each digit is concatenated three times.

original number=-2997 , n=3

-2997 = -222-999-999-777 and here each digit is concatenated three times.

"""

# My Solution

def check_concatenated_sum(num, n):
    try:
        if num < 0: num = num * -1
        sum = 0
        for i in str(num):
            sum += int(i * n)
    except:
        return False
        
    return sum == num

# Other Solutions

def check_concatenated_sum(n, r):
    return abs(n) == sum(int(e*r) for e in str(abs(n)) if r) 

def check_concatenated_sum(num, l):
    return sum([int(x*l) for x in str(abs(num))]) == abs(num) if l>0 else False

