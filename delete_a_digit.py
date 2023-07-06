# Delete a Digit - Codewars 6kyu

"""
Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example
For n = 152, the output should be 52;

For n = 1001, the output should be 101.

Input/Output
[input] integer n

Constraints: 10 ≤ n ≤ 1000000.

[output] an integer

"""
# My Solution

def delete_digit(n):
    string = str(n)
    maximum = 0
    for i in range(len(string)):
        curr = string.replace(string[i], '', 1)
        if int(curr) > maximum:
            maximum = int(curr)
    return maximum

# Other Solution

def delete_digit(n):
    s = str(n)
    return int(max(s[:i] + s[i+1:] for i in range(len(s))))