N = int(input())
A = list(map(int, input().split()))

mod = 10**9+ 7

from collections import Counter
c = Counter(A)

if N % 2 == 1:
    d = {i:2 for i in range(2, N, 2)}
    d[0] = 1
else:
    d = {i:2 for i in range(1, N, 2)}

if d != c:
    print(0)
    exit()
    
else:
    ans = pow(2, N//2, mod)
    print(ans)
    