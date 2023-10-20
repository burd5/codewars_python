# Sort Colors (leetcode)

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

"""


# 3 pointer solution

class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        runner = 0
        left_partition = 0
        right_partition = len(a) - 1
        while runner <= right_partition:
            if a[runner] == 0:
                a[runner], a[left_partition] = a[left_partition], a[runner]
                runner += 1
                left_partition += 1
            elif a[runner] == 1:
                runner += 1
            else:
                a[runner], a[right_partition] = a[right_partition], a[runner]
                right_partition -= 1
        return a
    
# Other Solutions

class Solution(object):
    def sortColors(self, nums):
        # Keep three counter to count 0s, 1s and 2s...
        count0s = 0
        count1s = 0
        count2s = 0
        # Traverse the array & Count the number of 0s, 1s and 2s in the array...
        for idx in range(len(nums)):
            # If the element is 0 then increase count0s...
            if nums[idx] == 0:
                count0s += 1
            # If the element is 1 then increase count1s...
            elif nums[idx] == 1:
                count1s += 1
            # If the element is 2 then increase count2s...
            elif nums[idx] == 2:
                count2s += 1
        # Update the array
        idx = 0;
        # Store all the 0s in the beginning...
        while (count0s > 0):
            nums[idx] = 0
            idx += 1
            count0s -= 1
        # Then store all the 1s...
        while (count1s > 0):
            nums[idx] = 1
            idx += 1
            count1s -= 1
        # Finally store all the 2s...
        while (count2s > 0):
            nums[idx] = 2
            idx += 1
            count2s -= 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

def sortColors(self, nums: List[int]) -> None:
    counts = [0, 0, 0]
    for i in nums:
        counts[i] += 1
    
    i = 0
    for k in range(3):
        while counts[k] > 0:
            nums[i] = k
            i += 1
            counts[k] -= 1