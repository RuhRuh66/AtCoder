N, S = map(int, input().split())

ans = 0

for i in range(1, N+1):
    if S-i > 0:
        if S-i <= N:
            ans += (S-i)
        else:
            ans += N

    else:
        break
print(ans)