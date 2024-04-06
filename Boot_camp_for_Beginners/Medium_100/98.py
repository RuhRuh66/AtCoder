N, P = map(int, input().split())

import math

ma = math.ceil(math.pow(P, 1/N))+1

if N == 1:
    print(P)
    exit()
    
elif N > P or N > 2912:
        print(1)
        exit()
else:
    gcd = 1
    for k in range(2, ma):
        l = pow(k, N)
        q, mod = divmod(P, l)
        if mod == 0:
            gcd = k
    print(gcd)
            


