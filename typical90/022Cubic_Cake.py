import math

A, B, C = map(int, input().split())
g = math.gcd(A, B)
g = math.gcd(g, C)

ans = (A+B+C)//g-3

print(ans)