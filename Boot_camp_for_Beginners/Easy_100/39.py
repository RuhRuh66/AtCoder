N = int(input())
A = []
for i in range(N):
    temp = int(input())
    A.append(temp)

B = sorted(A)
first = B[-1]
second = B[-2]


for i in range(N):
    t = A[i]
    if t == first:
        print(second)
    else:
        print(first)
        
