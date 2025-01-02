N = int(input())
stars = []
for i in range(N):
    x, y = map(int, input().split())
    stars.append([x, y])
    
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x1, y1 = stars[i][0], stars[i][1]
            x2, y2 = stars[j][0], stars[j][1]
            x3, y3 = stars[k][0], stars[k][1]
            
            a = x2-x1
            b = y2-y1
            c = x3-x1
            d = y3-y1
            
            if a*d == b*c:
                print('Yes')
                exit()
                
print('No')
            
        
            
        
    
    

        
        
        
    