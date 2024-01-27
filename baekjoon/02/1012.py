import sys
sys.setrecursionlimit(10000)
from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    # visited[y][x] = 1
    for i in range(4):
        ny,nx = y + dy[i], x + dx[i]
        if 0<= ny < n and 0 <= nx < m and g[ny][nx] == 1:
            g[ny][nx] = 0
            dfs(ny, nx)

T = int(input())
for _ in range(T):
    cnt = 0
    m, n, k = map(int, input().split())
    g = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        g[b][a] = 1
    
    for i in range(n):
        for j in range(m):
            if g[i][j] != 0:
                dfs(i, j)
                cnt += 1
    print(cnt)