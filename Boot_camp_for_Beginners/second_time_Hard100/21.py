n = int(input())
A = list(map(int, input().split()))

A.sort()

import bisect

m = A[-1]

n_prime = m/2

a = bisect.bisect_left(A, n_prime)

ans = []    
if a == 0:
    ans = [m, A[0]]
elif a == n-1:
    ans = [m, A[n-2]]
    
else:
    if n_prime-A[a-1] >= A[a]-n_prime:
        ans = [m, A[a]]
    else:
        ans = [m, A[a-1]]
        
print(*ans)