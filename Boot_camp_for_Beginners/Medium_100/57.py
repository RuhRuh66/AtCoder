N = int(input())
S = []

for i in range(N):
    temp = ''.join(sorted(input()))
    S.append(temp)

from collections import defaultdict
from math import comb

T = defaultdict(int)

for j in range(N):
    T[S[j]] += 1

ans = 0   
for k, v in T.items():
    if v >= 2:
        ans += comb(v, 2)
    else:
        continue
print(ans)