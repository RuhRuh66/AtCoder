N, K = map(int, input().split())

p = list(map(int, input().split()))

p1 = [(1+i)/2 for i in p]

start = 0
for i in range(K):
    start += p1[i]

ans = start
now = start
for i in range(N-K):
    temp = now - p1[i] + p1[i+K]
    ans = max(ans, temp)
    now = temp
    
print(ans)
    