import sys
input = sys.stdin.readline
import collections

#https://www.acmicpc.net/problem/1213
res = ''
mid=''

cnt = 0
w = input().rstrip()
lst = collections.Counter(w)

# {A:2}
for k,v in lst.items():
    if v % 2 == 1:
        cnt += 1
        mid = k
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()
for k,v in sorted(lst.items()):
    res += (k * (v // 2))
print(res + mid + res[::-1])