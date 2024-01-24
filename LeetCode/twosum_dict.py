# https://leetcode.com/problems/two-sum/description
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in memo:
                return [memo[needed], i]
            # {num:index}
            memo[num] = i
        
nums = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums, target))