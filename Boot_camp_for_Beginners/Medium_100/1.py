N = int(input())
A = [0]
visited = [False] * (N+1)
for i in range(N):
    temp = int(input())
    A.append(temp)
    
now = 1


for i in range(1, N+1):
    visited[now] = True
    next_city = A[now]
    if next_city == 2:
        print(i)
        exit()
    if visited[next_city] == False:
        now = next_city
        
    else:
        print(-1)
        exit()
        
print(-1)
        



    
        

        