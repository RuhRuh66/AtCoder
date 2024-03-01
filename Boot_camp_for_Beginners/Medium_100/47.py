N, P  = map(int, input().split())
A = list(map(int, input().split()))

import math

O = 0
E = 0
for i in range(N):
    if A[i] % 2 == 0:
        E += 1
    else:
        O += 1
        

ans = 0

if  P == 0:
    for j in range(0, O+1, 2):
        ans += math.comb(O, j)
    ans *= 2**E
else:
    for j in range(1, O+1, 2):
        ans += math.comb(O, j)
    ans *= 2**E
    
print(ans)