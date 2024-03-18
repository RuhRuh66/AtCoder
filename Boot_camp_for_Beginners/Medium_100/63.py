W, H, N = map(int, input().split())

LL = [0,0]
UR = [W, H]

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        if LL[0] <= x:
            LL = [x, LL[1]]
    elif a == 2:
        if UR[0] >= x:
            UR = [x, UR[1]]

    elif a == 3:
        if LL[1] <= y:
            LL = [LL[0], y]
    elif a == 4:
        if UR[1] >= y:
            UR = [UR[0], y]
            
if LL[0] >= UR[0] or LL[1] >= UR[1]:
    print(0)
else:
    print((UR[0]-LL[0])*(UR[1]-LL[1]))
