# https://leetcode.com/problems/two-sum/description
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: [i, j]
        return None
    
nums = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums, target))