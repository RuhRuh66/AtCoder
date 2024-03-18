N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


from math import ceil

def plus(x, y):
    return ceil(x/y)*y -x

ans = 0
for i in range(N-1, -1, -1):
    temp = plus(A[i]+ans, B[i])
    ans += temp


print(ans)
    

