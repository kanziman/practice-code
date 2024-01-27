from collections import deque
import sys
read = sys.stdin.readline
n, m = map(int, (input().split()))
g = []

for i in range(n):
    g.append(list(map(int, read().rstrip())))

dy = [0,1,0,-1]
dx = [1,0,-1,0]
q = deque()
q.append((0, 0))
ny=nx=0

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and g[ny][nx] == 1:
            q.append((ny,nx))
            g[ny][nx] = g[y][x] + 1


print(g[n-1][m-1])
