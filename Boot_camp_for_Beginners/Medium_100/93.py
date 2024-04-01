N, M = map(int, input().split())

S_to_L = [[] for i in range(N)]
for i in range(M):
    temp = list(map(int, input().split()))
    K = temp[0]
    L = temp[1:]
    
    for j in range(K):
        S_to_L[L[j]-1].append(i+1)
        
P = list(map(int, input().split()))



ans = 0
for k in range(1<<N):
    score = [0] * M
    for l in range(N):
        if (k >> l) & 1 == 1:
            for m in S_to_L[l]:
                score[m-1] += 1
        
    flag = True
    for n in range(M):
        if score[n] % 2 == P[n]:
            continue
        else:
            flag = False
            break
    if flag:
        ans += 1
        
print(ans)
            
        

    
        
        
        