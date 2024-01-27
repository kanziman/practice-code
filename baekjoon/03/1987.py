r, c = map(int, input().split())

sets = [list(input()) for _ in range(r)]



al = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not sets[nx][ny] in al:
            al.add(sets[nx][ny])
            dfs(nx, ny, count+1)
            al.remove(sets[nx][ny])
            
al.add(sets[0][0])
dfs(0, 0, 1)
print(ans)