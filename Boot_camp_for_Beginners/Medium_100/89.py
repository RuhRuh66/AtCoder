N, M = map(int, input().split())

possibility = [False] * (N+1)
ball_count = [1] * (N+1)

possibility[1] = True

for i in range(M):
    a, b = map(int, input().split())
    ball_count[a] -= 1
    ball_count[b] += 1
    if possibility[a] == True:
        possibility[b] = True
    if ball_count[a] == 0:
        possibility[a] = False
        

ans = 0
for j in range(N+1):
    if possibility[j] == True:
        ans += 1
        
print(ans)
