N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

B = defaultdict(int)

for i in range(N):
    B[A[i]] += 1
    

ans = 0
for a, b in B.items():
    if a == b:
        continue
    elif a > b:
        ans += b
    else:
        ans += (b-a)
        
print(ans)
