# Fizz Buzz Sum

"""
Write a function fizz_buzz_sum to find the sum of all multiples of 3 or 5 below a target value.

For example, if the target value was 10, the multiples of 3 or 5 below 8 are 3, 5, 6, and 9.

"""

# My Solution

def fizz_buzz_sum(target):
  return sum([i for i in range(1, target) if i % 3 == 0 or i % 5 == 0])

# Other Solutions

def fizz_buzz_sum(target):
  sum = 0
  for i in range(target):
    if (i % 3 == 0) or (i % 5 == 0):
      sum += i
  return sum