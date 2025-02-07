a, b  = map(int, input().split())

ans = 1
base = a
while b > 0:
    if b & 1 == 1:
        ans = (ans *base) % 1000000007
    b >>= 1
    base = (base * base) % 1000000007
    
print(ans)
    