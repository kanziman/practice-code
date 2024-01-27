import sys
read = sys.stdin.readline

lst = [0]*26

for i in read().strip():
    lst[ord(i) - 97] += 1

print(*lst)