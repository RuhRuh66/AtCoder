N = int(input())
L = 0
R = 10**9
A= []
for i in range(N):
    x, l = map(int, input().split())
    s = x-l
    t = x+l
    A.append((s, t))
    
A.sort(key = lambda x: x[1])

print(A)