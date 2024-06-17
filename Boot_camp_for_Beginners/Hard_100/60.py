N = int(input())

from collections import defaultdict

D = defaultdict(int)

for i in range(1, N+1):
    head = int(str(i)[0])
    tail = int(str(i)[-1])
    D[(head, tail)] += 1
    
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += D[(i, j)] * D[(j, i)]

print(ans)