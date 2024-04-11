h, w = map(int, input().split())
S = [list(input()) for i in range(h)]
q = [[h*w] * w for i in range(h)]

q[0][0] = int(S[0][0] == '#')

for i in range(h):
    for j in range(w):
        if i+1 < h:
            q[i+1][j] = min(q[i+1][j], q[i][j]+int(S[i][j]=='.' and S[i+1][j] == '#'))
        if j+1 < w:
            q[i][j+1] = min(q[i][j+1], q[i][j]+int(S[i][j]=='.' and S[i][j+1] == '#'))


print(q[h-1][w-1])