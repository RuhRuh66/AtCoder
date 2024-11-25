N, X, Y = map(int, input().split())

X, Y = X-1, Y-1

ans = [0] * N

for i in range(N-1):
    for j in range(i+1, N):
        dist = min(j-i, (abs(i-X) + abs(j-Y) + 1))
        ans[dist] += 1
        
for i in range(1, N):
    print(ans[i])




    