N = int(input())

base = [[0] * 1001 for i in range(1001)]

for i in range(N):
    lx, ly, rx, ry = map(int, input().split())

    base[lx][ly] += 1
    base[lx][ry] -= 1
    base[rx][ly] -= 1
    base[rx][ry] += 1

for i in range(1001):
    for j in range(1, 1001):
        base[i][j] += base[i][j-1]
        
for i in range(1, 1001):
    for j in range(1001):
        base[i][j] += base[i-1][j]

ans = [0] * (N+1)

for i in range(1001):
    for j in range(1001):
        cnt = base[i][j]
        ans[cnt] += 1
        
print(*ans[1:], sep= '\n')