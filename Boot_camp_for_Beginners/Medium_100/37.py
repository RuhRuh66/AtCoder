N = int(input())
H = list(map(int, input().split()))

active = 0
ans = 0

for i in range(N):
    if H[i] >= active:
        active = H[i]
        ans += H[i]-active

    else:
        ans += active-H[i]
        active = H[i]

print(ans)