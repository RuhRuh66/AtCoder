H, W = map(int, input().split())

S = [[] for i in range(H)]

for i in range(H):
    temp = list(input())
    S[i] = temp

T = [[-1]*W for i in range(H)]

a = [-1, -1, -1, 0, 0, 1, 1, 1]
b = [-1, 0, 1, -1, 1, -1, 0, 1]

for j in range(H):
    for k in range(W):
        if S[j][k] == '#':
            T[j][k] = '#'
            
        else:
            count = 0
            for l in range(8):
                nj = j+a[l]
                nk = k+b[l]
                
                if nj <0 or nj >H-1:
                    continue
                if nk <0 or nk >W-1:
                    continue
                if S[nj][nk] == '#':
                    count += 1
            T[j][k] = str(count)
            

for i in range(H):
    result = ''.join(T[i])
    print(result)