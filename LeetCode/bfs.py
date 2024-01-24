from collections import deque

def bfs(graph, start):
    q = deque()
    q.append(start)
    visited = {start}

    while q:
        cur = q.popleft()   
        for next in graph[cur]:
            if next not in visited:
                q.append(next)
                visited[next] = True
    return visited
    
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

print(bfs(graph, start_v))
# 0 ,1 ,3, 6, 2, 7, 5, 4