N = int(input())
A = list(map(int, input().split()))

called = [False] * (N+1)
called[0] = True

for i, j in enumerate(A, start=1):
    if called[i] == True:
        continue
    else:
        called[j] = True
        
print(called.count(False))
a = [ i-1 for i, j in enumerate(called, start=1) if j == False]
print(*a)