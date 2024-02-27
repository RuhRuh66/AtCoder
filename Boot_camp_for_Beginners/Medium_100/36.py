N, X = map(int, input().split())

A = list(map(int, input().split()))

B = []
for i in range(N):
    temp = abs(A[i] - X)
    B.append(temp)
    
from math import gcd

ans = 0

if N == 1:
    ans = abs(A[0]-X)

else:
    ans = B[0]
    for i in range(1, N):
        ans = gcd(ans, B[i])
    
print(ans)
    
    

