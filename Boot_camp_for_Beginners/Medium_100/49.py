N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

B = defaultdict(int)

for i in range(N):
    B[A[i]] += 1
    
C = sorted(B.items(), reverse=True)


if C[0][1] >= 4:
    print(C[0][0]**2)
    exit()

D = []
for l, n in C:
    if n >= 2:
        D.append(l)

if len(D) >= 2:
    print(D[0]*D[1])
else:
    print(0)

