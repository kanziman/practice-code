from itertools import combinations
import sys

read = sys.stdin.readline
nums = [int(read()) for _ in range(9)]

# for i in nums:
#  for j in nums:
#      if i+j == sum(nums) - 100:
#          nums.remove(i)
#          nums.remove(j)
# for i in nums: print(i)

for i in combinations(nums, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
