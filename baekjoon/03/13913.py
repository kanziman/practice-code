from collections import deque
N, K = map(int,input().split())
visited = [0] * 200001
prev = [0] * 200001
result = 0

q = deque()
q.append(N)
cnt = 0 

while q:
    x = q.popleft()
    if x == K:
        result = visited[x]
        cnt += 1
        # f(x)
        break
    
    for next in [x-1, x+1, x*2]:
        if 0 <= next <= 200000 and (visited[next] == 0):
            visited[next] = visited[x] + 1
            prev[next] = x
            q.append(next)

k = K
v = [k]
while k != N:
    k = prev[k]
    v.append(k)

print(result)
print(*v[::-1])

