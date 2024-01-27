import collections
n,c = map(int, input().split())

_list = list(map(int, input().split()))

# print(collections.Counter(_list))

count = {}
for i,v in enumerate(_list):
    if v not in count:
        count[v] = [0,i]
    count[v][0] += 1

# frequency
count = sorted(count.items(), key = lambda x: (-x[1][0],x[1][1]))

res = []
for k,v in count:
    res += [k]*v[0]
print(*res)