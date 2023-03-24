T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

import math
import numpy as np

for i in range(Q):
    E = int(input())
    theta = math.pi*2*(E/T)
    chokudai = np.array([X, Y, 0])
    me = np.array([0, -0.5*L*math.sin(theta), -0.5*L*(math.cos(theta)-1)])
    me2 = np.array([0, -0.5*L*math.sin(theta), 0])


    b = (X**2 +  (-0.5*L*math.sin(theta)-Y)**2)**0.5

    
    height = -0.5*L*(math.cos(theta)-1)
    
    ans = math.atan(height/b) /math.pi*180
    print(ans)
   
    
    