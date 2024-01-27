a = list(input())
for i in range(len(a)):
    if a[i].isupper(): a[i] = chr(65 + ((ord(a[i])) -65 +13) % 26)
    if a[i].islower(): a[i] = chr(97 + ((ord(a[i])) -97 +13) % 26)
print(''.join(a))