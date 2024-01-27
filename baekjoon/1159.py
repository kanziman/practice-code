arr = [input()[0] for _ in range(int(input()))]
f = 1
for i in range(26):
    if arr.count(chr(i+97)) >= 5:
        f = 0
        print(chr(i+97), end='')

if f: print('PREDAJA')
