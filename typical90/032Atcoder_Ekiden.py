N = int(input())
A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)
    
connectivity = [[True]*N for i in range(N)]
for i in range(N):
    connectivity[i][i] = False

M = int(input())
for i in range(M):
    X, Y = map(int, input().split())
    X -=1
    Y -=1
    connectivity[X][Y] = False
    connectivity[Y][X] = False
    
from itertools import permutations
patterns = permutations(range(N), N)

answer = 10**10
for pat in patterns:
    
    flag = True
    
    for i in range(N-1):
        if connectivity[pat[i]][pat[i+1]] == False:
            flag = False
            break
        
    if flag == True:
        rec = 0
        for i in range(N):
            rec += A[pat[i]][i]
                
        answer = min(answer, rec)    

if answer == 10**10:
    print(-1)   
else:
    print(answer)

    






    
        
    


