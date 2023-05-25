N, K = map(int, input().split())
a = list(map(int, input().split()))

cnt = dict()
r = 0
kind = 0

ans = 0

for l in range(N):
    while r < N and kind <= K:
        if a[r] not in cnt:
            cnt[a[r]] = 0
        if cnt[a[r]] == 0:
            kind += 1
        cnt[a[r]] += 1
        r += 1
    ans = max(ans, r-l-1)
    if kind <= K:
        ans = max(ans, r-l)
    
    cnt[a[l]] -= 1
    if cnt[a[l]] == 0:
        kind -= 1

print(ans)