N, K = map(int, input().split())

def g1(x):
    temp = sorted(list(str(x)), reverse = True)
    return int(''.join(temp))

def g2(x):
    temp = sorted(list(str(x)))
    return int(''.join(temp))

def f(x):
    return g1(x) - g2(x)


a = [0] * (K+1)
a[0] = N
for i in range(1, K+1):
    a[i] = f(a[i-1])
    
print(a[K]) 