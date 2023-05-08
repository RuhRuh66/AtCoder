N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

from itertools import combinations

ans = 0
combs = combinations(A, 5)
for a, b, c, d, e in combs:
    if a % P * b % P * c % P * d % P * e % P == Q:
        ans += 1
        
print(ans)
