N = int(input())

lista = []
listxy = []

for _ in range(N):
    a = int(input())
    xy = [list(map(int, input().split())) for _ in range(a)]
    lista.append(a)
    listxy.append(xy)
    

ans = 0

for i in range(1<<N):
    flag = True
    temp =  0
    for j in range(N):
       if i>>j & 1 == 1:
            temp += 1
            for x, y in listxy[j]:
                if i>>(x-1) & 1 != y:
                    flag = False
    if flag:
        ans = max(ans, temp)
        
print(ans)
    
                
            


  
                   
                    

            
            
            
            
    
    
    
    