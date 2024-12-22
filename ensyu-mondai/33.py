ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())



def calc_vector(x0, y0, x1, y1):
    return x1-x0, y1-y0

def calc_dist(dot, line):
    ax, ay = dot
    bx, by, cx, cy = line
    BAx, BAy = calc_vector(bx, by, ax,ay)
    BCx, BCy = calc_vector(bx, by, cx, cy)
    CAx, CAy = calc_vector(cx, cy, ax, ay)
    CBx, CBy = calc_vector(cx, cy, bx, by)
    ABx, ABy = calc_vector(ax, ay, bx, by)
    ACx, ACy = calc_vector(ax, ay, cx, cy)
    
    
    if BAx*BCx + BAy*BCy <= 0:
        ans = (BAx ** 2 + BAy **2) ** 0.5
    elif CAx*CBx + CAy*CBy <= 0:
        ans = (CAx**2 + CAy**2) ** 0.5
    else:
        outer_pro = abs(ABx*ACy - ABy*ACx)
        length_BC = ((bx-cx)**2 + (by-cy)**2)**0.5
        ans = outer_pro/length_BC
        
    return ans

d = calc_dist((ax, ay), (bx, by, cx, cy))     

print(d)