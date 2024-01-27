
ret = 0
cnt = [0]*100
a,b,c = map(int, input().split())

for _ in range(3):
    s,e = map(int , input().split())
    for i in range(s,e):
        cnt[i] += 1
for i in cnt:
    if i:
        if i == 1: ret += a
        if i == 2: ret += b*2
        if i == 3: ret += c*3
print(ret)
    