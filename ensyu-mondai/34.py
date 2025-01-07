import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def bruit(array):
    ln_ar = len(array)
    mi = float('inf')
    for i in range(ln_ar):
        for j in range(i+1, ln_ar):
            mi = min(mi,distance(array[i], array[j]))
            
    return mi

def closest_points(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return bruit(ax)
    
    m = ln_ax //2
    midpoint = ax[m]
    
    lx = ax[:m]
    rx = ax[m:]
    
    ly = list()
    ry = list()
    
    for p in ay:
        if p[0] <= midpoint[0]:
            ly.append(p)
        else:
            ry.append(p)
            
    d1 = closest_points(lx, ly)
    d2 = closest_points(rx, ry)
    
    d = min(d1, d2)
    
    split = [point for point in ay if abs(point[0]-midpoint[0]) < d]
    
    return closest_points_in_split(split, d)

    
    
        
def closest_points_in_split(arr, d):
    ln_arr = len(arr)
    for i in range(ln_arr):
        for j in range(i+1, min(i+7, ln_arr)):
            if arr[j][1]-arr[i][1] < d:
                d = min(d, distance(arr[i], arr[j]))
                
    return d
                
                
def solve(array):
    ax = sorted(array, key = lambda x: x[0])
    ay = sorted(array, key=lambda x: x[1])
    return closest_points(ax, ay)
    
N = int(input())
array =[]
for i in range(N):
    a, b = map(int, input().split())
    array.append((a,b))
    
print(solve(array))