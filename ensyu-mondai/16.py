from math import gcd

N = int(input())
A = list(map(int, input().split()))

a = gcd(A[0], A[1])

for i in range(2, N):
    a = gcd(a, A[i])
    
print(a)