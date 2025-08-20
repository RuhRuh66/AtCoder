N = int(input())

c = 2
mod = 10
ans = 1

while N > 0:
    if N & 1 == 1:
        ans = (ans * c) % mod
    c = (c*c) % mod
    N >>= 1
    
print(ans)
        
        
