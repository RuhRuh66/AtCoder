def g1(x):
    x = str(x)
    xx = sorted(list(x), reverse= True)
    y = ''.join(xx)
    return int(y)
def g2(x):
    x = str(x)
    xx = sorted(list(x))
    y = ''.join(xx)
    return int(y)

def f(x):
    return g1(x) - g2(x)

N, K = map(int, input().split())

A =[-1]* (K+1)
A[0] = N

for i in range(1, K+1):
    A[i] = f(A[i-1])
    
print(A[K])