N, K = map(int, input().split())
A = [0]+list(map(int, input().split()))

visited = [-1] * (N+1)
move_count = 0

now_city = 1
visited[1] = 0

for i in range(10**6):
    now_city = A[now_city]
    move_count += 1
    
    if move_count == K:
        print(now_city)
        exit()
        
    if now_city not in visited:
    