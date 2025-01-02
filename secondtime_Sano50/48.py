N = int(input())

min_x = 10**10
max_x = -10**10
min_y = 10** 10
max_y = -10**10

for i in range(N):
    a, b = map(int, input().split())
    x = a+b
    y = a-b
    
    min_x = min(min_x, x)
    min_y =min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    
ans = max(max_x - min_x, max_y -min_y)

print(ans)