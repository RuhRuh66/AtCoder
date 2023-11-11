N = int(input())
P = list(map(int, input().split()))

mi = P[0]

ans = 0
for i in range(N):
    if P[i] <= mi:
        ans += 1
    mi = min(mi, P[i])

print(ans)