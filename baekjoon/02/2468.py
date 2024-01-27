import sys
sys.setrecursionlimit(100000)
n = int(input())
g = []

dy = [0,1,0,-1]
dx = [1,0,-1,0]

for _ in range(n):
    g.append(list(map(int, input().split())))

def dfs(y, x, h):
    visited[y][x] = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and g[ny][nx] > h and visited[ny][nx] == 0:
            dfs(ny, nx, h)
            
            
res = 1
for h in range(100):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if g[i][j] > h and  visited[i][j] == 0:
                dfs(i, j, h)
                cnt += 1
    res = max(res, cnt)
print(res)