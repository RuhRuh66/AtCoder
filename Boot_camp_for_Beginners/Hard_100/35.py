N, H = map(int, input().split())

A = []
I = 10**9
for i in range(N):
    a, b = map(int, input().split())
    A.append((a, I))
    A.append((b, 1))
    
A.sort(reverse=True)

from math import ceil

S = 0

ans = 0
for j in range(2*N):
    a, b = A[j]
    if S < H:
        if b == 1:
            S += a 
        else:
            ans = ceil((H-S)/a) + j
            print(ans)
            exit()
    else:
        print(j)
        exit()
        



    

    
