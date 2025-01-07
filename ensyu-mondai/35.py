import math

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

if r1<r2:
    r1, r2 = r2, r1
    
d = dist((x1, y1), (x2, y2))

if d<r1-r2:
    print(1)
elif d == r1-r2:
    print(2)

elif r1-r2 < d < r1+r2:
    print(3)
elif d == r1+r2:
    print(4)
else:
    print(5)
    
