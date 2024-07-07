N = int(input())

A = []
li = []


for j in range(N):
    a = int(input())
    x = [list(map(int, input().split())) for _ in range(a)]
    A.append(a)
    li.append(x)
    
print(A, li)