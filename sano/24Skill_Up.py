N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    temp = list(map(int, input().split()))
    C.append(temp[0])
    A.append(temp[1:])
    
skills = [0] * M

min_cost = 10 ** 10
flag = False
for i in range(1<<N):
    skills = [0]*M
    cost = 0
    for j in range(N):
       if i>>j & 1 == 1:
           cost += C[j]
           for k in range(M):
               skills[k] += A[j][k]
    if min(skills) < X:
           pass
    else:
        flag = True
        min_cost = min(min_cost, cost)

if flag == False:
    print(-1)
else:
    print(min_cost)
                
  

    