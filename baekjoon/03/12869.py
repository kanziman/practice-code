import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

scvs = list(map(int,input().split()))

scvs.sort()
attacks = [9,3,1]
visited = set()

ans = 20

def dfs(depth, lst):
    global ans
    if not lst:
        ans = min(ans, depth)
        return
    for attack in permutations(attacks[:len(lst)], len(lst)):
        temp = []
        for k in range(len(lst)):
            x = lst[k] - attack[k]
            if x > 0:
                temp.append(x)
        temp.sort()
        
        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            dfs(depth+1, temp)
            if not temp:
                visited.remove(tuple(temp))    
    
dfs(0,scvs)
print(ans)