N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    min_x = A[i]
    for j in range(i, N):
        min_x = min(min_x, A[j])
        temp = min_x * (j - i +1)
        ans = max(temp, ans)
        
print(ans)