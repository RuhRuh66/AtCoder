H, W = map(int, input().split())
graph = [list(input()) for i in range(H)]

ans = [[H*W] * W for _ in range(H)]


ans[0][0] = int(graph[0][0] == '#')

for i in range(H):
    for j in range(W):
        if i+1 < H:
            ans[i+1][j] = min(ans[i+1][j], ans[i][j] + int(graph[i][j] =='.' and graph[i+1][j] == '#'))
        if j+1 < W:
            ans[i][j+1] = min(ans[i][j+1], ans[i][j] + int(graph[i][j] == '.' and graph[i][j+1] == '#'))
    
    
print(ans[H-1][W-1])