N, A, B = map(int, input().split())

a = 0
for i in range(1, N+1):
    b = 0
    s  = str(i)
    S = list(s)
    for k in S:
        b += int(k)
    if A <= b <= B:
        a += i
        
print(a)
        
    