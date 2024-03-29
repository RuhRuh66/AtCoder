N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

T = defaultdict(int)

for i in range(N):
    T[A[i]] += 1
    
if len(T) == 3:
    U = list(T.items())
    if U[0][0] ^ U[1][0] ^ U[2][0] == 0:
        for i, j in T.items():
            if i != 0 and j == N//3:
                continue
            else:
                print('No')
                exit()
                
        print('Yes')
    else:
        print('No')
elif len(T) == 2:
    U = sorted(list(T.items()))
    if (U[0][0] == 0 and U[0][1] == N//3) and (U[1][0] != 0 and U[1][1] == 2*N//3):
        print('Yes')
    else:
        print('No')
elif len(T) == 1:
    if T[0] == N:
        print('Yes')
    else:
        print('No')
else:
    print('No')
    
