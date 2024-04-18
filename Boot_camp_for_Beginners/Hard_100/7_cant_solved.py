N, M = map(int, input().split())
A = list(map(int, input().split()))


A.sort()
B= []
for i in range(M):
    b, c = map(int, input().split())
    B.append((b, c))
    
B.sort(key = lambda x: x[1], reverse=True)

ans = 0
count = 0

for j in range(M):
    for i in range(B[j][0]):
        if count == N:
            print(ans)
            exit()
        if A[count] >= B[j][1]:
            print(ans+sum(A[count:]))
            exit()
        ans += B[j][1]
        count += 1
        
print(ans + sum(A[count:]))