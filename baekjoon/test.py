# import sys
# read = sys.stdin.readline

# T = int(input())
# N = int(input())

# res = 0
# for i in range(N):
#     a,b = map(int, input().split())
#     res += a*b
    
# print(res==T)

# print('Yes') if res==T else print('No')

# n,m = map(int, input().split())
# basket = [i for i in range(1,n+1)]
# temp = 0
# for x in range(m):
#   i,j = map(int, input().split())
#   temp = basket[i-1:j]
#   temp.reverse()
#   basket[i-1:j] = temp
#   print(basket)

# for x in range(n):
#   print(basket[x],end=" ")

print([1,2,3].pop(0))

N = int(input())
array = [[0] * 100 for _ in range(101)]  # 도화지 범위 초기화
for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

res = 0
for k in range(1,101):
  res = array[k]