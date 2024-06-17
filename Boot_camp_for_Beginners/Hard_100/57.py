N = int(input())

A = [0] + list(map(int, input().split()))

from itertools import accumulate
B = list(accumulate(A))

from collections import defaultdict
C = defaultdict(int)

for i in range(N+1):
    C[B[i]] += 1
    
    
ans = 0
for k in C.values():
    if k>=2:
        ans += k*(k-1)//2
    else:
        continue
    
print(ans)
    
 




            
            
