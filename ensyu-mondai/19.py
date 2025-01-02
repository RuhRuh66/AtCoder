from math import comb

N = int(input())

A = list(map(int, input().split()))

a = A.count(1)
b = A.count(2)
c = A.count(3)

ans = comb(a, 2) + comb(b, 2) + comb(c, 2)

print(ans)