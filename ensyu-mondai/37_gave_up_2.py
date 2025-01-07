def gaiseki(A, B):
    #ベクトルOAとOBの外積
    #正ならOAを反時計回りにまわしてOB
    #絶対値は平行四辺形の面積
    return A[0]*B[1] - A[1]*B[0]


A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))
D = tuple(map(int, input().split()))

def make(A, B):
    ax, ay = A
    bx, by = B
    return (bx-ax, by-ay)

AB = make(A, B)
AC = make(A, C)
AD = make(A, D)

CD = make(C, D)
CA = make(C, A)
CB = make(C, B)

if gaiseki(AB, AC) == gaiseki(AB, AD) == 0:
    # 直線
    
    def f(l1, r1, l2, r2):
        if l1 > r1:
            l1, r1 = r1, l1
        
        if l2 > r2:
            l2, r2 = r2, l2
        
        return max(l1, l2) <= min(r1, r2)
    
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    
    if f(x1, x2, x3, x4) and f(y1, y2, y3, y4):
        ans = "Yes"
    else:
        ans = "No" 
        
    
else:
    if gaiseki(AB, AC) * gaiseki(AB, AD) <= 0 and gaiseki(CD, CA) * gaiseki(CD, CB) <= 0:
        ans = "Yes"
    else:
        ans = "No"

print(ans)  
