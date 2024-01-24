#https://leetcode.com/problems/daily-temperatures/description/
from typing import List
class Solution:
    def daily_temperatures(self, temperatures: str) -> bool:
        ans = [0]* len(temperatures)
        stack = []
        
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp: 
                idx = stack.pop()[0]
                ans[idx] = day - idx
            stack.append((day, temp))
        return ans

s = Solution()
temperatures = [73,74,75,71,69,72,76,73]

print(s.daily_temperatures(temperatures))
