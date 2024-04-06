n = int(input())
v = list(map(int, input().split()))

from collections import defaultdict

V1 = defaultdict(int)
V2 = defaultdict(int)

for i in range(0, n, 2):
    V1[v[i]] += 1
for j in range(1, n, 2):
    V2[v[j]] += 1

V1s = list(sorted(V1.items(), key=lambda x: x[1], reverse=True))
V2s = list(sorted(V2.items(), key=lambda x: x[1], reverse=True))

if V1s[0][0] != V2s[0][0]:
    ans = n - V1s[0][1] - V2s[0][1]

else:
    if V1s[0][1] > V2s[0][1]:
        ans = n- V1s[0][1] - V2s[1][1]
    elif V1s[0][1] < V2s[0][1]:
        ans = n - V1s[1][1] - V2s[0][1]
    else:
        if len(V1s) == 1:
            ans = n//2
        else:
            ans = min((n-V1s[0][1]-V2s[1][1]), (n-V1s[1][1]-V2s[0][1]))

print(ans)