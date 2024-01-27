#https://www.acmicpc.net/source/share/1797670218184cc385194f46b1b967dd
cnt = 0
n  = int(input())
for i in range(n):
    t = []
    w = input()
    
    for j in w:
        if not t or t[-1] != j:
            t.append(j)
        else:
            t.pop()
    if len(t) == 0:
        cnt += 1

print(cnt)