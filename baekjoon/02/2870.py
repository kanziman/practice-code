n = int(input())


ans = []


# for _ in range(n):
#     result = ''
#     num = input()
#     for i in num:
#         if i.isdigit():
#             result += i
#         else:
#             if result != '':
#                 ans.append(int(result))
#                 result = ''
#     if result != '':
#         ans.append(int(result))

import re
for _ in range(n):
    s = input()
    lst = re.split('[a-z]', s)
    for v in lst:
        if v : ans.append(v)
    
ans.sort()
for i in ans:
    print(i)