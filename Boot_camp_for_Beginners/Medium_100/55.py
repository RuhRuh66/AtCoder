N, M = map(int, input().split())
A = []
B = []

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        A.append(b)
    elif b == N:
        B.append(a)
    else:
        continue

A = set(A)
B = set(B)

if A.intersection(B):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')