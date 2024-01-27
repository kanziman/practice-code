from collections import deque
N, K = map(int,input().split())
LIMIT = 500_000
visited = [[-1] * 2 for _ in range(LIMIT + 1)]
cnt = res = 0

if N == K:  # 시작부터 둘의 위치가 같을 경우 0 출력하고 종료
    print(0)
    exit()
    
q = []
q.append(N)

time = 1
K += time

while q:
    if K > LIMIT:  # 동생이 500,000을 넘어서면 탐색 종료
        break
    nextQ = []
    
    for x in q:
        for next in [x+1,x-1,x*2]:
            if 0<= next <= 500000 and visited[x][time % 2] == -1:
                nextQ.append(next)
                visited[next][time % 2] = time
            
    if visited[K][time % 2] != -1:
        print(time)
        exit()
    
    time += 1
    K += time
    q = nextQ
print(-1)