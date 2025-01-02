N = int(input())

if N % 2 == 1:
    print(0)
    exit()
ans = 0

q = 10
while N >= q:
    ans += N//q
    q *= 5
    
print(ans)
