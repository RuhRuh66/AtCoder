N = int(input())
L = 0
R = 10**9
A= []
for i in range(N):
    x, l = map(int, input().split())
    s = x-l
    t = x+l
    
    if s <= 0:
        s = 0
    if t >= 10**9:
        t = 10**9
    
    A.append((t, s))
    
A.sort()

discard = 0
prev = A[0]

for i in range(1,N):
    if A[i][1] < prev[0]:
        discard += 1
    else:
        prev = A[i]
print(N-discard)
    