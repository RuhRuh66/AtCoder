N = int(input())
A = list(map(int, input().split()))
Ma = max(A)
Mi  =min(A)

ans = 10 ** 9
for i in range(Mi, Ma+1):
    temp = 0
    for j in range(N):
        temp += (A[j]-i)**2
    ans = min(ans, temp)
    
print(ans)
        
