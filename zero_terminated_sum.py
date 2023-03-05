"""
Zero Terminated Sum
Mary has another puzzle book, and it's up to you to help her out! This book is filled with zero-terminated substrings, and you have to find the substring with the largest sum of its digits. For example, one puzzle looks like this:

"72102450111111090"
Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums of their digits are 10, 11, 6, and 9 respectively. Therefore, the substring with the largest sum of its digits is 245, and its sum is 11.

Write a function largest_sum which takes a string and returns the maximum of the sums of the substrings. In the example above, your function should return 11.

Notes:
A substring can have length 0. For example, 123004560 has three substrings, and the middle one has length 0.
All inputs will be valid strings of digits, and the last digit will always be 0.

"""


def largest_sum(s):
    substrings = s.split('0')
    new_strings = list(filter(None, substrings))
  
    all_sums = []
    
    for element in new_strings:
        sum = 0
        for number in element:
            sum += int(number)
        all_sums.append(sum)
            

    
    return 0 if len(all_sums) == 0 else max(all_sums)

# pretty/short solution

def largest_sum(s):
    return max(sum(map(int,x)) for x in s.split('0'))