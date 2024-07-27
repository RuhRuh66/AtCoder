N = int(input())
M = []
for i in range(N):
    x, y, h = map(int, input().split())
    M.append((x, y, h))

M.sort(key = lambda x: x[2], reverse= True)



for i in range(101):
    for j in range(101):
        flag = True
        H = M[0][2] + abs(M[0][0]-i) + abs(M[0][1]-j)
        
        for k in range(1, N):
            if M[k][2] != max((H-abs(M[k][0]-i)-abs(M[k][1]-j)), 0):
                flag = False
                break
                
        if flag == True:
            print(i, j, H)  
        
         
                


        