from collections import deque

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = []

def bfs(y,x):
    q = deque()
    q.append((y, x))
    union = []
    union.append((y, x))
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 > ny or ny >= n or 0 > nx or nx >= n: continue
            if l <= abs(a[ny][nx] - a[y][x]) <= r and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny,nx))
                union.append((ny,nx))
    return union

res = 0
while True:
    visited = [[0]*n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                
            if len(country) > 1:
                flag = 1
                people = sum(a[y][x] for y,x in country ) // len(country)
                
                for y, x in country:
                    a[y][x] = people
                    
    if flag == 0:
        print(res)
        break
    res += 1