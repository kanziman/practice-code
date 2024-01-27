n,m = map(int, input().split())

j = int(input())

start = 1
ans = 0

for _ in range(j):
    a = int(input())
    
    if start <= a <= start + m - 1:
        continue
    elif a < start:
        ans += start - a
        start -= start - a
    else:
        ans += a - (start + m - 1)
        start += a - (start + m - 1)
print(ans)