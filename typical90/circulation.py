N = int(input())
dest = [[] for i in range(N+1)]
for j in range(1, N):
    a, b = map(int, input().split())
    dest[a].append(b)
    dest[b].append(a)
    
print(dest)
