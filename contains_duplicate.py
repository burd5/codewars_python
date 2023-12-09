# Contains Duplicate

"""
Given an list of integers called input, return True if any value appears at least twice in the array. Return False if every element in the input list is distinct.

For example, if the input list was [1,3,5,7,1], then return True because the number 1 shows up twice.

However, if the input was [1,3,5,7] then return False, because every element of the list is distinct.

"""

# My Solution

def contains_duplicate_1(input)-> bool:
  return len(set(input)) != len(input)

# Other Solution

def contains_duplicate_2(input):
  input.sort()
  for i in range(len(input)-1):
      if (input[i] == input[i+1]):
          return True
  return False

def contains_duplicate_3(input):
  seen = {}
  for i in input:
    if i in seen:
      return True
    seen[i] = True
  return False
