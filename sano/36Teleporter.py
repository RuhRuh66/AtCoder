N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

visited = [-1] * (N+1)
visited[1] = 0
now_city = 1

moved_count = 0

for i in range(10**6):
    moved_count += 1
    now_city = A[now_city]
    
    if moved_count == K:
        print(now_city)
        exit()
        
    if visited[now_city] < 0:
        visited[now_city] = moved_count
        
    else:
        break

cycle = moved_count - visited[now_city]

K -= visited[now_city]
K %= cycle

for i in range(K):
    now_city =  A[now_city]
    
print(now_city)
        
        