N = int(input())

amari_total = 0
amari_1 = 0
amari_2 = 0

keta = len(str(N))

while N > 0:
    K = N % 10 % 3
    amari_total += K
    if K == 1:
        amari_1 += 1
    elif K == 2:
        amari_2 += 1
    else:
        pass
    N //= 10
    
if amari_total % 3 == 0:
    ans = 0
elif amari_total % 3 == 1:
    if amari_1 >= 1 and keta > 1:
        ans = 1
    elif amari_2 >= 2 and keta > 2:
        ans = 2
    else:
        ans = -1
else:
    if amari_2 >= 1 and keta >1:
        ans = 1
    elif amari_1 >= 2 and keta > 2:
        ans = 2
    else:
        ans = -1
        
print(ans)