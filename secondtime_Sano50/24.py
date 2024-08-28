N, M, X = map(int, input().split())

books = [list(map(int, input().split())) for i in range(N)]

ans = 10**9
for i in range(1<<N):
    skills = [0] * M
    costs = 0
    for j in range(N):
        if i>>j & 1 == 1:
            costs += books[j][0]
            for k in range(M):
                skills[k] += books[j][k+1]
                
    if min(skills) >= X:
        ans = min(ans, costs)
if ans == 10**9:
    print(-1)
    exit()
        
print(ans)