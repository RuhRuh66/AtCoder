from collections import Counter

N = int(input())
D = list(map(int, input().split()))
mod = 998244353

E = dict(Counter(D))
l = len(E)

F = list(sorted(E.items()))


if D[0] != 0 or D.count(0) >= 2:
    print(0)
    exit()

if F[0][1] != 1 or F[-1][0] != l-1:
    print(0)
    exit()
    
ans = 1
for i in range(1, l):
    ans *= pow(F[i-1][1], F[i][1], mod) 
    
print(ans%mod)

