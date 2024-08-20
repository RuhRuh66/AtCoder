H, W = map(int, input().split())

A = [list(map(int, input().split())) for i in range(H)]

count = 0
moves = []

for i in range(H):
    for j in range(W):
        if A[i][j] % 2 == 0:
            continue
        else:
            if j != W-1:
                A[i][j+1] += 1
                moves.append([i+1, j+1, i+1, j+2])
                count += 1
                
            else:
                if i == H-1:
                    continue
                else:
                    A[i+1][j] += 1
                    moves.append([i+1,j+1, i+2, j+1])
                    count += 1

print(count)
for k in range(count):
    print(*moves[k])
                
