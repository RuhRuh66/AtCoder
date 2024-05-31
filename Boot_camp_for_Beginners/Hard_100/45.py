N = 10**5

P = [True] * (N+1)
P[0] = P[1] = False
for i in range(2, N+1):
    if P[i] == True:
        for j in range(i*i, N+1, i):
            P[j] = False
            
S = [0] * (N+1)

for i in range(3, N+1, 2):
    if P[i] and P[(i+1)//2]:
        S[i] += 1
        
from itertools import accumulate

S = list(accumulate(S))

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(S[r]-S[l-1])













    
    
    