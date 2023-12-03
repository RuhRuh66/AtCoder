H, W = map(int, input().split())

C = []
for i in range(H):
    temp = list(input())
    C.append(temp)
    C.append(temp)
    
    
for j in range(2*H):
    print(*C[j], sep='')
