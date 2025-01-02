N, K = map(int, input().split())
P = [0]+list(map(int, input().split()))

ex_p = []
for i in range(N):
    temp = (1+P[i])/2
    ex_p.append(temp)
    
from itertools import accumulate

P2 = accumulate(ex_p)

for j in range(N