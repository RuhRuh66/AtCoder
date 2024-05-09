N = int(input())
A = list(map(int, input().split()))

A.sort()

from itertools import accumulate

B = list(accumulate(A))


temp = -1

for i in range(N-1):
    if B[i] * 2 < A[i+1]:
        temp = i
        
ans = N-temp-1

print(ans)