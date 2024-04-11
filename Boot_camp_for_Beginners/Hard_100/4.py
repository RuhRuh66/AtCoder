
a, b, x = map(int, input().split())

if a % x == 0:
    
    l = a //x
else:
    l = a//x + 1
    
r = b//x

ans = r - l + 1

print(ans)
