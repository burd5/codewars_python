"""



"""

# my solution - o(n2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
                
# faster solution

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i in range(len(nums)):
        if nums[i] in hash_table:
            return [hash_table[nums[i]], i]
        else:
            hash_table[target - nums[i]] = i