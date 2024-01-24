from typing import List

#dict
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         res = 0
#         dict= {}
#         for num in nums:
#             dict[num] = True
        
#         for num in dict:
#             if num - 1 not in dict:
#                 cnt = 1
#                 next = num + 1
#                 while next in dict:
#                     cnt += 1
#                     next += 1
#                 res = max (cnt, res)
#         return res
    

#set
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        _set = defaultdict(list)
        print(_set)
        for num in _set:
            if num-1 not in _set:
                len = 1
                while num + len in _set:
                    len += 1
                res = max(res, len)
        return res
        
            
nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))

