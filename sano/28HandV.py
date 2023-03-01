H, W, K = map(int, input().split())
C = []
for i in range(H):
    temp = list(input())
    C.append(temp)
    
ans = 0
for i in range(1<<H):
    for j in range(1<<W):
        count = 0
        for k in range(H):
            for l in range(W):
                if i >> k & 1 == 0 and j >> l & 1 == 0:
                    if C[k][l] == '#':
                        count += 1
        if count == K:
            ans += 1
        
print(ans)