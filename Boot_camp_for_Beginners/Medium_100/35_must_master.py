def number(l, u, m):
    return u//m - (l-1)//m

A, B, C, D = map(int, input().split())

from math import gcd

lcm = C * D // gcd(C, D)

totals = B-A+1

ans = totals - number(A, B, C) - number(A, B, D) + number(A, B, lcm)

print(ans)

