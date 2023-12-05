# Factorial Formula

"""
https://datalemur.com/questions/python-factorial-formula

"""

# My Solution

def factorial(n):
  sum = 1
  for i in range(1, n + 1):
    sum *= i
    
  return sum

# Recursive Solution

def factorial(n):
  if n == 0:
      return 1
  else:
      return n * factorial(n - 1)
  
  