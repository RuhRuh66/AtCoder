N = int(input())

S = input()
mod = 10**9 + 7

from collections import defaultdict

T = defaultdict(int)


for i in range(N):
    T[S[i]] += 1


ans = 1
for s, j in T.items():
    ans = (ans * (j+1)) % mod
    
print(ans-1)
    
