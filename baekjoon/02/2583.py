import sys
sys.setrecursionlimit(100000)
n,m,k = map(int, input().split())
a = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())    
    for i in range(y1, y2):
        for j in range(x1, x2):
            a[i][j] += 1
            
dy=[0,1,0,-1]
dx=[1,0,-1,0]
def dfs(y, x):
    visited[y][x] = 1
    ret = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if(0 <= ny < n and 0 <= nx < m and a[ny][nx] == 0 and visited[ny][nx] == 0 ):
            ret += dfs(ny, nx)
    return ret
cnt = 0
lst = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and visited[i][j] == 0:
            lst.append(dfs(i,j))
            cnt += 1

print(cnt)
print(*sorted(lst))