from collections import deque
N, K = map(int,input().split())
visited = [0] * 200001
result = 0


q = deque()
q.append(N)
cnt = 0 

while q:
    x = q.popleft()
    if x == K:
        result = visited[x]
        cnt += 1
        continue
    
    for i in [x-1, x+1, x*2]:
        if 0 <= i <= 100000 and (visited[i] == 0 or visited[i] == visited[x] + 1):
            visited[i] = visited[x] + 1
            q.append(i)

print(result)
print(cnt)