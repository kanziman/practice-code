#https://leetcode.com/problems/valid-parentheses/description/
from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            '(':')',
            '{':'}',
            '[':']'
        }
            
        for c in s:
            if c in dict:
                stack.append(c)
            elif c == dict[stack[-1]]:
                stack.pop()
            else: return False
        
        return len(stack) == 0
    

s = Solution()
print(s.isValid("()[]{}"))