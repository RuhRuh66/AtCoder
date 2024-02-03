G = []
for i in range(3):
    temp = list(map(int, input().split()))
    G.append(temp)

for i in range(2):
    for j in range(2):
        if G[i][j]-G[i+1][j] == G[i][j+1] -G[i+1][j+1]:
            continue
        