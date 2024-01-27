from collections import deque

n,m = map(int, input().split())

a = [list(map(int, input().strip())) for _ in range((n))]
visited = [[0]*m for _ in range((n))]

d = [(1,0),(0,1),(-1,0),(0,-1)]
visited[0][0] = 1

def bfs():
    q = deque()
    q = [(0,0)]
    while q:
        y,x = q.pop()
        for dy,dx in d:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < n and 0 <= nx < m and a[ny][nx] == 1:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny,nx))
bfs()
print(visited[n-1][m-1])

    