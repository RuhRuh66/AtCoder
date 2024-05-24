N = int(input())


queries = [[] for i in range(N+1)]


for j in range(N):
    A = int(input())
    for i in range(A):
        x, y = map(int, input().split())
        queries[j+1].append((x,y))



for i in range(1<<N):
    assump = [0] * (N+1)
    judge = [-1] * (N+1)
   
    for j in range(N):
        if i>>j & 1 == 1:
            assump[j+1] = 1
            for x, y  in queries[j+1]:
                judge[x] = y
    
    
    
    
        
          


                    
                    
            
            
            
            
    
    
    
    