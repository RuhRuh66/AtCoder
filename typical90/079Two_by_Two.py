H, W = map(int, input().split())

A = []
B = []
for _ in range(H):
    temp = list(map(int, input().split()))
    A.append(temp)
for _ in range(H, 2*H):
    temp = list(map(int, input().split()))
    B.append(temp)
    
ans = 0
for i in range(H-1):
    for j in range(W-1):
        if A[i][j] == B[i][j]:
            continue
        else:
            dif = B[i][j] - A[i][j]
            A[i][j] += dif
            A[i+1][j] += dif
            A[i][j+1] += dif
            A[i+1][j+1]+= dif
            ans += abs(dif)
            
        if j == W-2:
            if A[i][W-1] == B[i][W-1]:
                continue
            else:
                print('No')
                exit()
                
        if i == H-2:
            if A[H-1][j] == B[H-1][j]:
                continue
            else:
                print('No')
                exit() 
print('Yes')
print(ans)
            