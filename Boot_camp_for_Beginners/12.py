N = int(input())

D = list(map(int, input().split()))

from collections import defaultdict

E = defaultdict(int)
mod = 998244353

for i in range(N):
    E[D[i]] += 1
    
# F = sorted(E.items(), key = lambda x: x[0])

L = len(E.items())



if D[0] != 0 or E[0] != 1:
    print(0)
    exit()
    



else:
    ans = 1
    for j in range(1, L):
        
        if E[j] == 0:
            print(0)
            exit()
        else:
            ans = (ans * (E[j-1]**E[j]))%mod
            
            
    print(ans)
        

