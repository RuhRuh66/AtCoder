N  = int(input())

val = []

for i in range(N):
    A, B = map(int, input().split())
    v = A+B
    val.append([v, A, B])
    
val.sort(key = lambda x:x[0], reverse=True)

T = 0
A = 0

for i in range(N):
    if i % 2 == 0:
        T += val[i][1]
    else:
        A += val[i][2]

print(T-A)
