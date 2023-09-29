h, w = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(h)]
from collections import Counter

ans = 0
for i in range(1, 1<<h):
    select_h  =[]
    for j in range(h):
        if i >> j & 1 == 1:
            select_h.append(j)
    

    
    if len(select_h) == 1:
        c = Counter(grid[select_h[0]])
        ans = max(ans, c.most_common()[0][1])
        
    else:
        count_w = dict()
        for col in range(w):
            val =  grid[select_h[0]][col]
            if all(grid[row][col] == val for row in select_h):
                if val in count_w:
                    count_w[val] += 1
                else:
                    count_w[val] = 1
                    
        

        if not count_w:
            max_w = 0
        else:
            max_w = max(count_w.values())
            
        ans = max(ans,  max_w * len(select_h))
        
print(ans)