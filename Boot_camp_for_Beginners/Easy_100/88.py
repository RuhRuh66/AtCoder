from collections import defaultdict

S = defaultdict(int)
T = defaultdict(int)

N = int(input())
for i in range(N):
    s = input()
    S[s] += 1

M = int(input())
for j in range(M):
    t = input()
    T[t] += 1
    

for k in T.items():
    if k[0] in S:
        S[k[0]] -= k[1]
        
U = sorted(S.items(), key= lambda x: x[1], reverse=True)

if U[0][1] <= 0:
    print(0)
    exit()
else:
    print(U[0][1])