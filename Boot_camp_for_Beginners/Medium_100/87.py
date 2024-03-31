N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()

else:
    excesses = {}
    shortage = {}

    for i in range(N):
        if A[i] >= B[i]:
            excesses[i] = A[i] - B[i]
        else:
            shortage[i] = B[i] - A[i]
            
from collections import deque
E = deque()
S = deque()
            
exc = sorted(excesses.items(), key = lambda x: x[1], reverse = True)
shr = sorted(shortage.items(), key = lambda x: x[1], reverse = True)


if len(shr) == 0:
    print(0)
    exit()
    
E.extend(exc)
S.extend(shr)

count = 0
holding = 0
must_pay = 0
while S:
    must_pay = S.popleft()[1]
    count += 1
    while holding < must_pay:
        holding += E.popleft()[1]
        count += 1
    holding -= must_pay
    
print(count)
        
    

    
    
    

        
        