N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    A.append(list(input()))
for j in range(M):
    B.append(list(input()))
    

for k in range(N-M+1):
    for l in range(N-M+1):
        flag = True
        for m in range(M):
            if A[k+m][l:l+M] == B[m]:
                continue
            else:
                flag = False
                break
        if flag == True:
            print('Yes')
            exit()
            
print('No')