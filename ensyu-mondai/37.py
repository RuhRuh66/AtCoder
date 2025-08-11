<<<<<<< HEAD
pos = []
for i in range(4):
    x, y = map(int, input().split())
    pos.append([x, y])
    
def cross(A, B):
    return (A[0]*B[1]-A[1]*B[0])

def vec(A, B):
    return [B[0]-A[0], B[1]-A[1]]

def on_segment(X, Y, Z):
    if not min(X[0], Y[0]) <= Z[0] <= max(X[0], Y[0]):
        return False
    if not min(X[1], Y[1]) <= Z[1] <= max(X[1], Y[1]):
        return False
    return True 

AB = vec(pos[0], pos[1])
AC = vec(pos[0], pos[2])
AD = vec(pos[0], pos[3])

CD = vec(pos[2], pos[3])
CA = vec(pos[2], pos[0])
CB = vec(pos[2], pos[1])

t1 = cross(AB, AC)
t2 = cross(AB, AD)
t3 = cross(CD, CA)
t4 = cross(CD, CB)

ans = 'No'

if t1*t2 <0 and t3*t4 <0:
    ans = 'Yes'

if t1 == 0 and on_segment(pos[0], pos[1], pos[2]):
    ans = 'Yes'
        
if t2 == 0 and on_segment(pos[0], pos[1], pos[3]):
    ans = 'Yes'
if t3 == 0 and on_segment(pos[2], pos[3], pos[0]):
    ans = 'Yes'
if t4 == 0 and on_segment(pos[2], pos[3], pos[1]):
    ans = 'Yes'
    
print(ans)
=======
import numpy as np

a = np.array([0, 1, 0])
b = np.array([1, 0, 0])

c = np.cross(a, b)
print(c)
>>>>>>> 2d2d37e (37 from mac)
