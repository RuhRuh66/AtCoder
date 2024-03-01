N = int(input())

A = list(map(int, input().split()))

from collections import deque

B = deque()




status = 'f'
for i in range(N):
    if status == 'f':
        B.append(A[i])
        status = 'b'
    else:
        B.appendleft(A[i])
        status = 'f'
        
if status == 'f':
    print(*B)
    
else:
    B = reversed(B)
    print(*B)
        

