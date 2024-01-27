#https://www.acmicpc.net/problem/1620
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for i in range(1, 1+n):
    name = input().rstrip()
    d[i] = name
    d[name] = i

for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(d[int(q)])
    else:
        print(d[q])