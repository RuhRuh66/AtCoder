X, Y = map(int, input().split())
if (2*X-Y) % 3 != 0 or (2*Y-X) % 3 != 0:
    print(0)
    exit()
else:
    b = (2*X-Y)//3
    a = (2*Y-X)//3

if a < 0 or b < 0:
    print(0)
    exit()

mod = 1000000007



def combin(c, d):
    numer = 1
    denom = 1
    for i in range(c, c-d, -1):
        numer = (numer * i) % mod
    for j in range(d, 1, -1):
        denom = (denom *j) % mod
        
    return (numer * pow(denom, -1, mod)) % mod
    

print(combin(a+b, b))
    