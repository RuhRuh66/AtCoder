h, w = list(map(int , input().split()))
c = []
for i in range(h):
    c.append(input())
    
move = ((0, 1), (-1, 0), (0, -1), (1, 0))

ans = 0

def dfs(start, now, cnt):
    global ans
    check.add(now)
    for h, w in move:
        hh, ww = h+now[0], w+now[1]
        if 0 <= hh < h and 0 <= ww < W and c[hh][ww] != '#':
            