N = int(input())

A = [0] + list(map(int, input().split()))

B = [0]*(N+1)

for i in range(N, 0, -1):
    sums = 0
    for j in range(i+i, N+1, i):
        sums ^= B[j]
    B[i] = sums^A[i]

s = sum(B)

C = enumerate(B)
D = []
for a, b in C:
    if b == 1:
        D.append(a)
        
print(s)
print(*D)