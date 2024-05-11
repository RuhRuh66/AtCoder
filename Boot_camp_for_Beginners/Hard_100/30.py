N, K = map(int, input().split())
A = list(map(int, input().split()))

M = max(A)

from math import gcd

g = gcd(*A)

if g == 1:
    if K <= M:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
        
        
else:
    if K > M:
        print('IMPOSSIBLE')
    else:
        if K % g == 0:
            print('POSSIBLE')
        else:
            print('IMPOSSIBLE')
        