N  = int(input())

from math import lcm
ans = 1
for i in range(N):
    a = int(input())
    ans = lcm(ans, a)

print(ans)

