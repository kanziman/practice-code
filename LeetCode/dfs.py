from collections import deque
visited = {}

def dfs(v):
    print(v)
    visited[v] = True
    for next in graph[v]:
        if next not in visited:
            dfs(next)

graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

start_v = 0
print(dfs(start_v))
# 0 ,1 ,3, 6, 2, 7, 5, 4