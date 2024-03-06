W, H, x, y = map(int, input().split())

ans = W * H / 2

if x == W/2 and y == H/2:
    p = 1
else:
    p = 0
    
print(ans, p)


