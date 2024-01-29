H, W = map(int, input().split())

G = []
for i in range(H):
    temp = input()
    G.append(temp)

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        if G[i][j] == '#':
            flag = False
            for k in range(4):
                if i+dh[k] <0 or i + dh[k] >= H or j+dw[k] <0 or j+dw[k]>=W:
                    continue
                else:
                    if G[i+dh[k]][j+dw[k]] == '#':
                        flag = True
            if flag == False:
                print('No')
                exit()

print('Yes')