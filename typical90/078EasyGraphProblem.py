N, M  = map(int, input().split())

from collections import defaultdict

s = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    s[b].append(a)

ans = 0       
for val in s.values():
    if len(val) == 1:
        ans += 1


print(ans)
