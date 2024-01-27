#https://acmicpc.net/problem/9375
import sys

read = sys.stdin.readline
for i in range(int(read())):
    res  = 1
    dict = {}
    for j in range(int(read())):
        _, gear = read().split()
        
        if gear in dict:
            dict[gear] += 1
        else:
            dict[gear] = 1
        
    for k in dict:
        res *= (dict[k] + 1)
    print('ans>>',res-1)
        
        