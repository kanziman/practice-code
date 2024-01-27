from collections import deque

n,m = map(int, input().split())
a= [list(map(str, input())) for _ in range(n)]
d = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(y, x):
    visited = [[0]*m for _ in range(n)]
    visited[y][x] = 1
    q = deque()
    q.append((y,x))
    mx = 0
    while q:
        y,x = q.popleft()
        for dy,dx in d:
            ny,nx = y+ dy, x+dx
            if 0<= ny < n and 0<= nx < m and a[ny][nx] == 'L' and visited[ny][nx] == 0:                
                visited[ny][nx] = visited[y][x] + 1; 
                q.append((ny,nx))
                mx = max(mx, visited[ny][nx]);
    return mx - 1
           
res = 0     
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            res = max(res, bfs(i,j))
print(res)