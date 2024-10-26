N, M = map(int, input().split())
A = list(map(int, input().split()))

A_sort = sorted(A)

q = []

for i in range(M):
    b, c = map(int, input().split())
    q.append((b, c))

q.sort(key=lambda x: x[1], reverse=True)

now = 0
ans = 0
for j in range(M):
    
        
    b, c = q[j]
    for k in range(b):
        if A_sort[now] < c:
            ans += c
            now += 1
            if now == N:
                print(ans)
                exit()
        else:
            break
          
print(ans + sum(A_sort[now:]))
            
    
    

