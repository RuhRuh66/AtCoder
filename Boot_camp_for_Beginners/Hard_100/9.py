N, M = map(int, input().split())
import re

A = []
B = []
for i in range(N):
    temp = input()
    A.append(temp)
for j in range(M):
    temp2 = input()
    B.append(temp2)
    
for k in range(N-M+1):
    st = set(i for i in range(N))
    for l in range(M):
        s = re.compile(B[l])
        t = re.finditer(s, A[k+l])
        temp = set(i.start() for i in t)
        st &= temp
    if len(st) == 0:
        continue
    else:
        print('Yes')
        exit()
print('No')
    

        
        