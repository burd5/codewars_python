# Balanced Number

"""
A balanced number is a number where the sum of digits to the left of the middle digit(s) and the sum of digits to the right of the middle digit(s) are equal.

If the number has an odd number of digits, then there is only one middle digit. (For example, 92645 has one middle digit, 6.) Otherwise, there are two middle digits. (For example, the middle digits of 1301 are 3 and 0.)

The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5.

The task
Given a number, find if it is balanced, and return the string "Balanced" or "Not Balanced" accordingly. The passed number will always be positive.

Examples
7 ==> return "Balanced"
Explanation:
middle digit(s): 7
sum of all digits to the left of the middle digit(s) -> 0
sum of all digits to the right of the middle digit(s) -> 0
0 and 0 are equal, so it's balanced.

"""

# My Solution

def balanced_num(number):
    if len(str(number)) % 2 != 0:
        middle = len(str(number))//2
        left = sum([int(x) for i,x in enumerate(str(number)) if i < middle])
        right = sum([int(x) for i,x in enumerate(str(number)) if i > middle])
        return "Balanced" if left == right else "Not Balanced"
    if len(str(number)) % 2 == 0:
        lmid = len(str(number))//2 - 1
        rmid = len(str(number))//2
        left = sum([int(x) for i,x in enumerate(str(number)) if i < lmid])
        right = sum([int(x) for i,x in enumerate(str(number)) if i > rmid])
        return "Balanced" if left == right else "Not Balanced"
    

# Other Solutions

def balancedNum(n):
    s = str(n)
    l = (len(s)-1)//2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"

balanced_num = balancedNum


def balanced_num(number):
    number = [int(n) for n in str(number)]
    left, right = 0, 0
  
    while len(number) > 2 :
        left += number.pop(0)
        right += number.pop(-1)

    return "Balanced" if left == right else "Not Balanced"

