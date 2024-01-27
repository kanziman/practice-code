n,k = map(int, input().split())
ret = -1000000
a = list(map(int, input().split()))
psum = [0]*100000

for i in range(1, len(a)+1):
    psum[i] = psum[i-1] + a[i-1]

for i, v in enumerate(a):
    i += k
    ret = max(ret, psum[i] - psum[i-k])
# for i in range(k, len(a)+k):
#     ret = max(ret, psum[i] - psum[i-k])
print(ret)