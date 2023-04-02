N, K = map(int, input().split())
A = []
for i in range(N):
    x, y = map(int, input().split())
    x -= y
    A.append(x)
    A.append(y)
    
import heapq

A_minus =[]
for i in A:
    i *= -1
    A_minus.append(i)
    
    
heapq.heapify(A_minus)
time = 0
ans = 0
while time < K:
    ans += heapq.heappop(A_minus)
    time += 1
    
print(-ans)
    



    
