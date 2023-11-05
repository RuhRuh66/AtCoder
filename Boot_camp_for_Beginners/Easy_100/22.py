N, x = map(int, input().split())
A = list(map(int, input().split()))
import sys

A.sort()
sums = sum(A)

ans = 0

if sums == x:
    ans = N
    print(ans)
    sys.exit()
    
if sums < x:
    ans = N-1
    print(ans)
    sys.exit()

for i in A:
    if x - i >= 0:
        ans += 1
        x -= i
        
print(ans)




    
    
    