from itertools import combinations
n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
    
house=[]
chick=[]
res = 999999
for i in range(n):
    for j in range(n):
        if a[i][j] == 1: house.append([i,j])
        if a[i][j] == 2: chick.append([i,j])


for c in combinations(chick, m):
    temp = 0
    for h in house:
        d = 999
        for j in range(m):
            d = min(d, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += d
    res = min(res, temp)

print(res)