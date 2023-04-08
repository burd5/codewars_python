"""
This is a problem that involves adding numbers to items in a list. In a list you will have to add the item's remainder when divided by a given divisor to each item.

For example if the item is 40 and the divisor is 3 you would have to add 1 since 40 minus the closest multiple of 3 which is 39 is 1. So the 40 in the list will become 41. You would have to return the modified list in this problem.

For this problem you will receive a divisor called div as well as simple list of whole numbers called nums. Good luck and happy coding.

Examples
nums = [2, 7, 5, 9, 100, 34, 32, 0], div = 3
  ==>  [4, 8, 7, 9, 101, 35, 34, 0] 

nums = [1000, 999, 998, 997], div = 5
   ==> [1000, 1003, 1001, 999]

"""

# my solution

def solve(nums, div):
    # answer arr to append items to
    answer = []
    # for loop to loop through nums
    for num in nums:
        if num < div:
            answer.append(num * 2)
        elif num/div == 0:
            answer.append(num)
        else:
            answer.append(num + num % div)
    return answer

# other solution

def solve(nums,div):
    return [x + x % div for x in nums]