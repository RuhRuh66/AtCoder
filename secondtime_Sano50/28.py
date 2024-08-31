H, W, K  = map(int, input().split())
c = [list(str(input())) for _ in range(H)]

from copy import deepcopy


ans = 0
for i in range(1<<H):
    for j in range(1<<W):
        d = deepcopy(c)
        for k in range(H):
            if i >> k & 1 == 1:
                d[k] = ['r'] * W
                
        for l in range(W):
            if j >> l & 1 == 1:
                for m in range(H):
                    d[m][l] = 'r'
        cnt = 0        
        for n in range(H):
            cnt += d[n].count('#')
        
        if cnt == K:
            ans += 1
            
print(ans)
        
        
            